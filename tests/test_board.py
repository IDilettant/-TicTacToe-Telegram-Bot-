"""Tests of board."""
import tictactoe.scripts.board as board
import tictactoe.scripts.player as player

empty_board = [
    [None for row in range(board.SIDE_SIZE)] for col in range(board.SIDE_SIZE)
]
full_of_x = [
    [
        player.x_char for row in range(board.SIDE_SIZE)
    ] for col in range(board.SIDE_SIZE)
]
two_empty_state = [
    [1, 2, 1],
    [2, 1, 1],
    [2, None, None],
]
backwards_diagonal = [
    [2, None, None],
    [None, 2, None],
    [None, None, 2],
]
forwards_diagonal = [
    [None, None, 1],
    [None, 1, None],
    [1, None, None],
]


def test_get_legal_moves():
    """Test getting coordinates of possible moves."""
    assert len(board.get_legal_moves(empty_board)) == 9
    assert len(board.get_legal_moves(two_empty_state)) == 2
    assert bool(board.get_legal_moves(full_of_x)) is False
    assert board.get_legal_moves(two_empty_state) == [(2, 1), (2, 2)]


def test_make_move():
    """Test changing board current state based on the move made."""
    assert board.make_move(empty_board, (0, 0), player.x_char) == [
        [1, None, None],
        [None, None, None],
        [None, None, None],
    ]
    assert board.make_move(empty_board, (2, 2), player.o_char) == [
        [1, None, None],
        [None, None, None],
        [None, None, 2],
    ]
    assert board.make_move(full_of_x, (1, 1), player.o_char) == full_of_x


def test_has_row_win():
    """Test checking for a win horizontally."""
    assert board.has_row_win(full_of_x) is True
    assert board.has_row_win(empty_board) is False
    assert board.has_row_win(two_empty_state) is False


def test_has_col_win():
    """Test checking for a win vertically."""
    assert board.has_col_win(full_of_x) is True
    assert board.has_col_win(empty_board) is False
    assert board.has_col_win(two_empty_state) is False


def test_has_diagonal_win():
    """Test checking for a win diagonally."""
    assert board.has_diagonal_win(full_of_x) is True
    assert board.has_diagonal_win(empty_board) is False
    assert board.has_diagonal_win(two_empty_state) is False
    assert board.has_diagonal_win(backwards_diagonal) is True
    assert board.has_diagonal_win(forwards_diagonal) is True


def test_has_win():
    """Test checking for the win."""
    assert board.has_win(full_of_x) is True
    assert board.has_win(empty_board) is False
    assert board.has_win(two_empty_state) is False
    assert board.has_win(backwards_diagonal) is True
    assert board.has_win(forwards_diagonal) is True
