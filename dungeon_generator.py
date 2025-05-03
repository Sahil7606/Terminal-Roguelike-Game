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

    def split(self, direction, offset) -> tuple['Rect']:
        # if direction == 'y':
            # Calculate partition point
            # Calculate new rect bounds

        pass
            

        
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
    def __init__(self, area, left, right, room = None):
        self.area = area
        self.left = left
        self.right = right

# Maybe this would be better as a function
class Dungeon_Generator:
    """
    Attributes:
        bsp_root (BSP_Node): the root of the bsp tree to be split into rooms

    """
    pass