"""Basic module for bot logic."""


class Node(object):
    """Node of tree of possible states of game board."""

    def __init__(self, move=0, value=0, depth=0):  # noqa: WPS110
        """Build a class instance.

        Args:
            move (int): coordinate of board cell
            value (int): outcome significance of board state
            depth (int): sequential number of the tree level
        """
        self.move = move
        self.value = value  # noqa: WPS110
        self.depth = depth
