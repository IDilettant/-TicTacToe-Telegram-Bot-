"""Player module."""
from enum import Enum


class Mark(Enum):
    """Mark for cells of game board.

    Contains the definitions of the game symbol for each player and empty cells
    """

    x_char = ' x '
    o_char = ' o '
    empty_cell = ' . '

    @property
    def switch_char(self):
        """Change char for the current player."""
        return Mark.x_char if self == Mark.o_char else Mark.o_char
