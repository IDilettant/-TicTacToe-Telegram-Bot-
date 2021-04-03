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
    [2, 2, 1],
    [2, 1, 1],
    [1, None, None],
]


def test_get_legal_moves():
    """Test getting coordinates of possible moves."""
    assert len(board.get_legal_moves(empty_board)) == 9
    assert board.get_legal_moves(full_of_x) == 0
    assert len(board.get_legal_moves(two_empty_state)) == 2
    assert board.get_legal_moves(two_empty_state) == [[2, 1], [2, 2]]


def test_make_move():
    """Test changing board current state based on the move made."""
    assert board.make_move(empty_board, (0, 0), player.x_char) == [
        [1, None, None],
        [None, None, None],
        [None, None, None],
    ]
    assert board.make_move(empty_board, (2, 2), player.o_char) == [
        [None, None, None],
        [None, None, None],
        [None, None, 2],
    ]
    assert board.make_move(full_of_x, (1, 1), player.o_char) == full_of_x
