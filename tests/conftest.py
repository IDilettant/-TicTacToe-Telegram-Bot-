"""Fixtures module."""
import pytest


@pytest.fixture
def board_states():  # noqa: WPS210
    """Contain different board states.

    Returns:
        board states
    """
    board_size = 9
    empty = ' . '
    x_char = ' x '
    full_of_x = {
        cell: x_char for cell in range(board_size)
    }
    row = {
        0: empty,
        1: empty,
        2: empty,
        3: empty,
        4: empty,
        5: empty,
        6: x_char,
        7: x_char,
        8: x_char,
    }
    col = {
        0: empty,
        1: empty,
        2: x_char,
        3: empty,
        4: empty,
        5: x_char,
        6: empty,
        7: empty,
        8: x_char,
    }
    backwards_diagonal = {
        0: x_char,
        1: empty,
        2: empty,
        3: empty,
        4: x_char,
        5: empty,
        6: empty,
        7: empty,
        8: x_char,
    }
    forwards_diagonal = {
        0: empty,
        1: empty,
        2: x_char,
        3: empty,
        4: x_char,
        5: empty,
        6: x_char,
        7: empty,
        8: empty,
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
    side_size = 3
    empty = ' . '
    x_char = ' x '
    full_of_x = [
        [
            x_char for _ in range(side_size)
        ] for _ in range(side_size)
    ]
    row = [
        [empty, empty, empty],
        [empty, empty, empty],
        [x_char, x_char, x_char],
    ]
    col = [
        [empty, empty, x_char],  # noqa: WPS204
        [empty, empty, x_char],
        [empty, empty, x_char],
    ]
    backwards_diagonal = [
        [x_char, empty, empty],
        [empty, x_char, empty],
        [empty, empty, x_char],
    ]
    forwards_diagonal = [
        [empty, empty, x_char],
        [empty, x_char, empty],
        [x_char, empty, empty],
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
    board_size = 9
    full_of_x = list(range(board_size))
    row = [6, 7, 8]
    col = [2, 5, 8]
    backwards_diagonal = [0, 4, 8]
    forwards_diagonal = [2, 4, 6]
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
        Tie state of game board
    """
    x_char = ' x '
    o_char = ' o '
    return {
        0: x_char,
        1: o_char,
        2: x_char,
        3: x_char,
        4: o_char,
        5: x_char,
        6: o_char,
        7: x_char,
        8: o_char,
    }
