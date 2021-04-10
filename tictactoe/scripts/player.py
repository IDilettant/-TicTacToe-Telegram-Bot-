"""Player module."""
from enum import Enum


class Player(Enum):
    """Player class.

    Contains the definitions of the game symbol for each player
    and the method of changing the turn
    """

    x_char = ' x '
    o_char = ' o '
    none = ' . '

    def switch_turn(self):
        """Change the current player.

        Returns:
            Actual player symbol
        """
        return Player.x_char if self == Player.o_char else Player.o_char
