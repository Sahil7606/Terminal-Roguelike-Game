# Add Point class, to project
class Rect:
    """
    Used to represent areas on the map for BSP nodes and rooms

    Attributes:
        x, y (int): the position of the top-left corner of the rectangle
        width, height: the width and height of the rectangle

    Methods:
        center() -> (tuple): returns the center of the rectangle in the form (x, y)
    """
    pass

class BSP_Node:
    """
    Nodes for the BSP tree used for generation

    Attributes:
        rect (Rect): the rectangle this node represents
        left, right (BSP_Node): child nodes
        room (Rect): the room placed in this region (only for leaves)
    """
    pass

class Dungeon_Generator:
    pass