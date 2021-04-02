"""Player module."""

PLAYER_X = 1
PLAYER_O = 2


def switch_player(player):
    """Change current player.

    Args:
        player (int): current player

    Returns:
        another player
    """
    return PLAYER_X if player == PLAYER_O else PLAYER_O
