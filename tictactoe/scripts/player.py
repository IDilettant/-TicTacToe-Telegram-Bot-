"""Player module."""
from tictactoe.scripts.board import get_legal_moves

x_char = 1
o_char = 2


def switch_player(player):
    """Change current player.

    Args:
        player (int): current player

    Returns:
        another player
    """
    return x_char if player == o_char else o_char


def make_move(current_state, row, col, player):
    """Change board current state based on the move made.

    Args:
        current_state (list): board current state
        row (int): board row index
        col (int): board col index
        player (int): current player

    Returns:
        Board current state
    """
    if current_state[row][col] in get_legal_moves(current_state):
        current_state[row][col] = player
    return current_state
