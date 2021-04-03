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


def make_move(current_state, row, col, player_mark):
    """Change board current state based on the move made.

    Args:
        current_state (list): board current state
        row (int): board row index
        col (int): board col index
        player_mark (int): mark of current player

    Returns:
        Board current state
    """
    next_move = current_state[row][col]
    legal_moves = get_legal_moves(current_state)
    if next_move in legal_moves:
        current_state[row][col] = player_mark
    return current_state
