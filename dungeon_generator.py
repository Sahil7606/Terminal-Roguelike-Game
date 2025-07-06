from utils.types import Point

class Rect:
    """
    Used to represent areas on the map for BSP nodes and rooms

    Attributes:
        x, y (int): the position of the bottom-left corner of the rectangle
        width, height: the width and height of the rectangle

    Methods:
        center() -> (Point): returns the center of the rectangle in the form (x, y)
        intersects(other: Rect) -> bool: returns whether or not the rectangle intersects with the other
        split(direction, offset) -> tuple(Rect): splits rectangle and returns a tuple with the resulting rectangles
    """

    def __init__(self, x, y, width, height):
        self.pos = Point(x, y)
        self.width = width
        self.height = height

    @property
    def x(self): return self.pos.x

    @property
    def y(self): return self.pos.y

    @property
    def bottom_right(self) -> Point:
        return Point(self.x + self.width, self.y)

    @property
    def top_left(self) -> Point:
        return Point(self.x, self.y + self.height)

    @property
    def top_right(self) -> Point:
        return Point(self.x + self.width, self.y + self.height)

    @property
    def center(self):
        """
        Returns a Point object representing the center of the rectangle
        """
        return Point(self.pos.x + self.width // 2, self.pos.y + self.height // 2)
    
    def __contains__(self, other: Point):
        """
        Checks if a point is inside of the current rectangle

        Args:
            other (Point): the Point or the other Rect to check for

        Returns:
            (bool): True if the Point is inside the Rect, False if not
        """

        return (
            self.x <= other.x < self.x + self.width and
            self.y <= other.y < self.y + self.height
        )

    def split(self, direction: str, offset: float) -> tuple['Rect']:
        if direction == 'y':
            offset_point = self.x + int(self.width * offset)
            rect_1 = Rect(self.x, self.y, self.width - (self.bottom_right.x - offset_point), self.height)
            rect_2 = Rect(offset_point, self.y, self.width - (offset_point - self.x), self.height)
        else:
            offset_point = self.y + int(self.height * offset)
            rect_1 = Rect(self.x, self.y, self.width, self.height - (self.top_left.y - offset_point))
            rect_2 = Rect(self.x, offset_point, self.width, self.height - (offset_point - self.y))

        return (rect_1, rect_2)
            
class BSP_Node:
    """
    Nodes for the BSP tree used for generation

    Attributes:
        area (Rect): the rectangle this node represents
        left, right (BSP_Node): child nodes
        room (Rect): the room placed in this region (only for leaves)

    Methods:
        split(): Splits the area of the node and assigns those spaces to the chilren of the node
    """

    def __init__(self, area, left = None, right = None, room = None):
        self.area = area
        self.left = left
        self.right = right

    def split(self, direction: str, offset: float, min_size: int) -> None:
        if (self.left or self.right):
            return "Cannot be split"
        
        if self.area.width <= min_size or self.area.height <= min_size:
            return "Cannot be split"

        areas = self.area.split(direction, offset)
        self.left = BSP_Node(areas[0])
        self.right = BSP_Node(areas[1])
        
# Need to define a min size and bias when splitting
# divide height / width then use the ratio to make a bias in the random choice

import random

def generate_partitions(level: list[BSP_Node], depth: int):
    if depth == 0:
        return level
    
    def get_split_bias(node: BSP_Node) -> list|None:
        proportion = node.area.height / node.area.width
        temp = []

        if proportion < 1:
            proportion = 1 / proportion
            temp = ['y'] * int(proportion // 2)
        else:
            temp = ['x'] * int(proportion // 2)

        if proportion >= 4:
            return None

        return ['x', 'y'] + temp

    
    next_level = []
    for node in level:
        split_bias = get_split_bias(node)
        if not split_bias:
            continue
        node.split(random.choice(split_bias), random.uniform(0.4, 0.6), 1)
        next_level.append(node.left)
        next_level.append(node.right)

    return generate_partitions(next_level, depth - 1)