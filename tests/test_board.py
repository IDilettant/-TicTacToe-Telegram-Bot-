"""Tests for game board."""  # flake8: noqa
from tictactoe.scripts.board import Board
from tictactoe.scripts.mark import Mark


def test_make_move(board_states: list, moves_coordinate: list):
    """Test changing board current state based on the move made.

    Args:
        board_states: states of game board
        moves_coordinate: coordinates of moves
    """
    for case in zip(board_states, moves_coordinate):
        board = Board()
        state, moves = case
        for move in moves:
            board.make_move(move, Mark.x_char)
        assert board.current_state == state


def test_make_impossible_move():
    """Test changing board current state based on impossible move."""
    board = Board()
    board.make_move((board.side_size, board.side_size), Mark.x_char)
    for char in board.current_state.values():
        assert char != Mark.x_char.value


def test_make_move_for_full_of_o():
    """Test changing board full of Mark.o_char state based on the move made."""
    board = Board()
    full_of_o = dict.fromkeys(
        [(row, col) for row in range(board.side_size) for col in range(board.side_size)],  # noqa: E501
        Mark.o_char,
    )
    for move, player in full_of_o.items():
        board.make_move(move, player)
    board.make_move((1, 1), Mark.x_char)
    assert board.current_state == full_of_o


def test_get_grid(moves_coordinate: list, grids: list):
    """Test getting a grid of the current state of game board.

    Args:
        grids: grids of game board
        moves_coordinate: coordinates of moves for board states
    """
    for case in zip(moves_coordinate, grids):
        board = Board()
        moves, grid = case
        for move in moves:
            board.make_move(move, Mark.x_char)
        assert board.get_grid() == grid


def test_line_has_match():
    """Test homogenic of the incoming sequence."""
    board = Board()
    assert board._line_has_match(  # noqa: WPS437
        [Mark.x_char, Mark.x_char, Mark.x_char],
    ) is True
    assert board._line_has_match(  # noqa: WPS437
        [Mark.o_char, Mark.o_char, Mark.o_char],
    ) is True
    assert board._line_has_match(  # noqa: WPS437
        [Mark.empty_cell, Mark.empty_cell, Mark.empty_cell],
    ) is False
    assert board._line_has_match([]) is False  # noqa: WPS437


def test_has_win(board_states: list):
    """Test checking board for the win.

    Args:
        board_states: states of game board

    """
    for state in board_states:
        board = Board()
        for move, player in state.items():
            board.make_move(move, player)
        assert board.has_win() is True


def test_tie_state_has_win(tie_state: dict):
    """Test checking tie state of game board for the win.

    Args:
        tie_state : tie state of game board
    """
    board = Board()
    for move, player in tie_state.items():
        board.make_move(move, player)
    assert board.has_win() is False


def test_empty_board_has_win():
    """Test checking empty state of game board for the win."""
    board = Board()
    assert board.has_win() is False


def test_legal_moves(tie_state: dict):
    """Test getting possible moves for current board state.

    Args:
        tie_state: tie state of game board
    """
    board = Board()
    assert len(board.legal_moves) == board.side_size ** 2
    for move, player in tie_state.items():
        board.make_move(move, player)
    assert not board.legal_moves


def test_get_last_move():
    """Test getting the last made move."""
    board = Board()
    board.make_move((1, 1), Mark.x_char)
    assert board.last_move == (1, 1)


def test_get_view(tie_state):
    board = Board()
    tie_state_view = '\u274c\u274c\u2b55\n\u2b55\u2b55\u274c\n\u274c\u274c\u2b55'
    board.current_state = tie_state
    view = board.get_view()
    assert view == tie_state_view
