"""Tests of board."""
from tictactoe.scripts.board import Board

X_CHAR = ' x '
O_CHAR = ' o '


def test_make_move(board_states, moves_coordinate):
    """Test changing board current state based on the move made.

    Args:
        board_states (list): states of game board
        moves_coordinate (list): coordinates of moves
    """
    for case in zip(board_states, moves_coordinate):
        board = Board()
        state, moves = case
        for move in moves:
            board.make_move(move, X_CHAR)
        assert board.current_state == state


def test_make_move_for_full_of_o():
    """Test changing board full of ' o ' state based on the move made."""
    board = Board()
    full_of_o = {cell: O_CHAR for cell in range(board.side_size ** 2)}
    for move, char in full_of_o.items():
        board.make_move(move, char)
    board.make_move(4, X_CHAR)
    assert board.current_state == full_of_o


def test_get_grid(moves_coordinate, grids):
    """Test getting a grid of the current state of game board.

    Args:
        grids (list): grids of game board
        moves_coordinate (list): coordinates of moves for board states
    """
    for case in zip(moves_coordinate, grids):
        board = Board()
        moves, grid = case
        for move in moves:
            board.make_move(move, X_CHAR)
        assert board.get_grid() == grid


def test_line_has_match():
    """Test homogenic of the incoming sequence."""
    board = Board()
    assert board._line_has_match(  # noqa: WPS437
        [X_CHAR, X_CHAR, X_CHAR],
    ) is True
    assert board._line_has_match(  # noqa: WPS437
        [O_CHAR, O_CHAR, O_CHAR],
    ) is True
    assert board._line_has_match([' . ', ' . ', ' . ']) is False  # noqa: WPS437
    assert board._line_has_match([]) is False  # noqa: WPS437


def test_has_win(board_states):
    """Test checking board for the win.

    Args:
        board_states (list): states of game board

    """
    for state in board_states:
        board = Board()
        for move, char in state.items():
            board.make_move(move, char)
        assert board.has_win() is True


def test_tie_state_has_win(tie_state):
    """Test checking tie state of game board for the win.

    Args:
        tie_state (dict): tie state of game board
    """
    board = Board()
    for move, char in tie_state.items():
        board.make_move(move, char)
    assert board.has_win() is False
