"""Player module."""

x_char = 1
o_char = 2


def switch_turn(player):
    """Change current player.

    Args:
        player (int): current player

    Returns:
        another player
    """
    return x_char if player == o_char else o_char
