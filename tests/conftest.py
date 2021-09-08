"""Fixtures module."""
import pytest
from tictactoe.board import Board
from tictactoe.mark import Mark


@pytest.fixture
def board_states():  # noqa: WPS210
    """Contain different board states.

    Returns:
        board states
    """
    board = Board()
    full_of_x = dict.fromkeys(
        [(row, col) for row in range(board.side_size) for col in range(board.side_size)],  # noqa: E501
        Mark.x_char,
    )
    row = {
        (0, 0): Mark.empty_cell,
        (1, 0): Mark.empty_cell,
        (0, 2): Mark.empty_cell,
        (0, 1): Mark.empty_cell,
        (1, 1): Mark.empty_cell,
        (1, 2): Mark.empty_cell,
        (2, 0): Mark.x_char,
        (2, 1): Mark.x_char,  # noqa: WPS204
        (2, 2): Mark.x_char,
    }
    col = {
        (0, 0): Mark.empty_cell,
        (1, 0): Mark.empty_cell,
        (0, 2): Mark.x_char,
        (0, 1): Mark.empty_cell,
        (1, 1): Mark.empty_cell,
        (1, 2): Mark.x_char,
        (2, 0): Mark.empty_cell,
        (2, 1): Mark.empty_cell,
        (2, 2): Mark.x_char,
    }
    backwards_diagonal = {
        (0, 0): Mark.x_char,
        (1, 0): Mark.empty_cell,
        (2, 0): Mark.empty_cell,
        (0, 1): Mark.empty_cell,
        (1, 1): Mark.x_char,
        (2, 1): Mark.empty_cell,
        (0, 2): Mark.empty_cell,
        (1, 2): Mark.empty_cell,
        (2, 2): Mark.x_char,
    }
    forwards_diagonal = {
        (0, 0): Mark.empty_cell,
        (1, 0): Mark.empty_cell,
        (2, 0): Mark.x_char,
        (0, 1): Mark.empty_cell,
        (1, 1): Mark.x_char,
        (2, 1): Mark.empty_cell,
        (0, 2): Mark.x_char,
        (1, 2): Mark.empty_cell,
        (2, 2): Mark.empty_cell,
    }
    return [
        full_of_x,
        row,
        col,
        backwards_diagonal,
        forwards_diagonal,
    ]


@pytest.fixture
def grids():  # noqa: WPS210
    """Contain different grids of game board.

    Returns:
        grids of board
    """
    board = Board()
    full_of_x = [
        [
            Mark.x_char for _ in range(board.side_size)
        ] for _ in range(board.side_size)
    ]
    row = [
        [Mark.empty_cell, Mark.empty_cell, Mark.empty_cell],
        [Mark.empty_cell, Mark.empty_cell, Mark.empty_cell],
        [Mark.x_char, Mark.x_char, Mark.x_char],
    ]
    col = [
        [  # noqa:WPS204
            Mark.empty_cell, Mark.empty_cell, Mark.x_char,
        ],
        [Mark.empty_cell, Mark.empty_cell, Mark.x_char],
        [Mark.empty_cell, Mark.empty_cell, Mark.x_char],
    ]
    backwards_diagonal = [
        [Mark.x_char, Mark.empty_cell, Mark.empty_cell],
        [Mark.empty_cell, Mark.x_char, Mark.empty_cell],
        [Mark.empty_cell, Mark.empty_cell, Mark.x_char],
    ]
    forwards_diagonal = [
        [Mark.empty_cell, Mark.empty_cell, Mark.x_char],
        [Mark.empty_cell, Mark.x_char, Mark.empty_cell],
        [Mark.x_char, Mark.empty_cell, Mark.empty_cell],
    ]
    return [
        full_of_x,
        row,
        col,
        backwards_diagonal,
        forwards_diagonal,
    ]


@pytest.fixture
def moves_coordinate():  # noqa: WPS210
    """Contain lists of coordinates to form board states.

    Returns:
        lists of coordinates
    """
    board = Board()
    full_of_x = [
        (row, col) for row in range(board.side_size) for col in range(board.side_size)  # noqa: E501
    ]
    row = [(2, 0), (2, 1), (2, 2)]
    col = [(0, 2), (1, 2), (2, 2)]
    backwards_diagonal = [(0, 0), (1, 1), (2, 2)]
    forwards_diagonal = [(0, 2), (1, 1), (2, 0)]
    return [
        full_of_x,
        row,
        col,
        backwards_diagonal,
        forwards_diagonal,
    ]


@pytest.fixture
def tie_state():
    """Contain tie state of game board.

    Returns:
        tie state of game board
    """
    return {
        (0, 0): Mark.x_char,
        (1, 0): Mark.o_char,
        (2, 0): Mark.x_char,
        (0, 1): Mark.x_char,
        (1, 1): Mark.o_char,
        (2, 1): Mark.x_char,
        (0, 2): Mark.o_char,
        (1, 2): Mark.x_char,
        (2, 2): Mark.o_char,
    }
