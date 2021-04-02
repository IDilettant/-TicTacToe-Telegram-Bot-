#!/usr/bin/env python
"""Basic module for bot logic."""

PLAYER_X = 1
PLAYER_O = 2
DIMENSION = 3
board_state = [[None for row in range(DIMENSION)] for col in range(DIMENSION)]
moves = []
marker_to_char = {
    None: ' . ',
    PLAYER_X: ' x ',
    PLAYER_O: ' o ',
}


def switch_player(player):
    """Change current player.

    Args:
        player: current player

    Returns:
        another player
    """
    return PLAYER_X if player == PLAYER_O else PLAYER_O


def show_board(current_state):
    """Print current state of board.

    Args:
        current_state (list): board current state
    """
    for row in range(DIMENSION):
        line = []
        for col in range(DIMENSION):
            line.append(marker_to_char[current_state[row][col]])
        print(''.join(line))


def has_row_win(current_state):
    """Check for a win horizontally.

    Args:
        current_state (list): board current state

    Returns:
        bool
    """
    for row in range(DIMENSION):
        unique_rows = set(current_state[row])
        if len(unique_rows) == 1:
            return unique_rows.pop() is None


def has_col_win(current_state):
    """Check for a win vertically.

    Args:
        current_state: board current state

    Returns:
        bool
    """
    for col in range(DIMENSION):
        unique_cols = set()
        for row in range(DIMENSION):
            unique_cols.add(current_state[row][col])
        if len(unique_cols) == 1:
            return unique_cols.pop() is None


def main():
    """Create main function."""
    show_board(board_state)  # noqa: WPS420


if __name__ == '__main__':
    main()
