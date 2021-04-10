"""Tests of board."""
from tictactoe.scripts.board import Board
from tictactoe.scripts.player import Player


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
            board.make_move(move, Player.x_char)
        assert board.current_state == state


def test_make_impossible_move():
    """Test changing board current state based on impossible move."""
    board = Board()
    board.make_move(len(board.current_state) + 1, Player.x_char)
    for char in board.current_state.values():
        assert char != Player.x_char.value


def test_make_move_for_full_of_o():
    """Test changing board full of ' o ' state based on the move made."""
    board = Board()
    full_of_o = {
        cell: Player.o_char for cell in range(
            board.side_size ** 2,
        )
    }
    for move, player in full_of_o.items():
        board.make_move(move, player)
    board.make_move(4, Player.x_char)
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
            board.make_move(move, Player.x_char)
        assert board.get_grid() == grid


def test_line_has_match():
    """Test homogenic of the incoming sequence."""
    board = Board()
    assert board._line_has_match(  # noqa: WPS437
        [' x ', ' x ', ' x '],
    ) is True
    assert board._line_has_match(  # noqa: WPS437
        [' o ', ' o ', ' o '],
    ) is True
    assert board._line_has_match(  # noqa: WPS437
        [' . ', ' . ', ' . '],
    ) is False
    assert board._line_has_match([]) is False  # noqa: WPS437


def test_has_win(board_states):
    """Test checking board for the win.

    Args:
        board_states (list): states of game board

    """
    for state in board_states:
        board = Board()
        for move, player in state.items():
            board.make_move(move, player)
        assert board.has_win() is True


def test_tie_state_has_win(tie_state):
    """Test checking tie state of game board for the win.

    Args:
        tie_state (dict): tie state of game board
    """
    board = Board()
    for move, player in tie_state.items():
        board.make_move(move, player)
    assert board.has_win() is False


def test_empty_board_has_win():
    """Test checking empty state of game board for the win."""
    board = Board()
    assert board.has_win() is False


def test_get_legal_moves(tie_state):
    """Test getting possible moves for current board state.

    Args:
        tie_state (dict): tie state of game board
    """
    board = Board()
    assert len(board.get_legal_moves()) == 9
    for move, player in tie_state.items():
        board.make_move(move, player)
    assert not board.get_legal_moves()


def test_get_last_move():
    """Test getting the last made move."""
    board = Board()
    board.make_move(9, Player.x_char)
    assert board.last_move() == 9
