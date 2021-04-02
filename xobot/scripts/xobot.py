#!/usr/bin/env python
"""Basic module for bot logic."""

PLAYER_X = 1
PLAYER_O = 2


def switch_player(player):
    """Change current player.

    Args:
        player: current player

    Returns:
        another player
    """
    return PLAYER_X if player == PLAYER_O else PLAYER_O


def main():
    """Create main function."""
    pass  # noqa: WPS420


if __name__ == '__main__':
    main()
