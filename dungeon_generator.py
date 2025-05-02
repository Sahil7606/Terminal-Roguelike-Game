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
    """

    def __init__(self, x, y, width, height):
        self.pos = Point(x, y)
        self.width = width
        self.height = height

    def get_corners(self):
        """
        Returns a list[Point] with all 4 corners of the rectangle in it
        """
        corners = [
            self.pos,
            Point(self.pos.x + self.width, self.pos.y),
            Point(self.pos.x, self.pos.y + self.height),
            Point(self.pos.x + self.width, self.pos.y + self.height)
        ]

        return corners

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
            self.pos.x <= other.x < self.pos.x + self.width and
            self.pos.y <= other.y < self.pos.y + self.height
        )
    
    def intersects(self, other: 'Rect') -> bool:
        """
        Checks if a rectangle overlaps the current rectangle

        Args:
            other (Rect): the other rectangle to check for overlap with

        Returns:
            (bool): True if they intersect, False if not
        """
        return not (
            self.pos.x + self.width <= other.pos.x or
            self.pos.x >= other.pos.x + other.width or
            self.pos.y + self.height <= other.pos.y or
            self.pos.y >= other.pos.y + other.height
        )
        
class BSP_Node:
    """
    Nodes for the BSP tree used for generation

    Attributes:
        area (Rect): the rectangle this node represents
        left, right (BSP_Node): child nodes
        room (Rect): the room placed in this region (only for leaves)
    """
    def __init__(self, area, left, right, room = None):
        self.area = area
        self.left = left
        self.right = right

class Dungeon_Generator:
    pass