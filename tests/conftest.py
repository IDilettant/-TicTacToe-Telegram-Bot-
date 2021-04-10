"""Fixtures module."""
import pytest
from tictactoe.scripts.player import Player


@pytest.fixture
def board_states():  # noqa: WPS210
    """Contain different board states.

    Returns:
        board states
    """
    board_size = 9
    full_of_x = {
        cell: Player.x_char for cell in range(board_size)
    }
    row = {
        0: Player.none,
        1: Player.none,
        2: Player.none,
        3: Player.none,
        4: Player.none,
        5: Player.none,
        6: Player.x_char,
        7: Player.x_char,
        8: Player.x_char,
    }
    col = {
        0: Player.none,
        1: Player.none,
        2: Player.x_char,
        3: Player.none,
        4: Player.none,
        5: Player.x_char,
        6: Player.none,
        7: Player.none,
        8: Player.x_char,
    }
    backwards_diagonal = {
        0: Player.x_char,
        1: Player.none,
        2: Player.none,
        3: Player.none,
        4: Player.x_char,
        5: Player.none,
        6: Player.none,
        7: Player.none,
        8: Player.x_char,
    }
    forwards_diagonal = {
        0: Player.none,
        1: Player.none,
        2: Player.x_char,
        3: Player.none,
        4: Player.x_char,
        5: Player.none,
        6: Player.x_char,
        7: Player.none,
        8: Player.none,
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
    full_of_x = [
        [
            Player.x_char.value for _ in range(side_size)
        ] for _ in range(side_size)
    ]
    row = [
        [Player.none.value, Player.none.value, Player.none.value],
        [Player.none.value, Player.none.value, Player.none.value],
        [Player.x_char.value, Player.x_char.value, Player.x_char.value],
    ]
    col = [
        [  # noqa:WPS204
            Player.none.value, Player.none.value, Player.x_char.value,
        ],
        [Player.none.value, Player.none.value, Player.x_char.value],
        [Player.none.value, Player.none.value, Player.x_char.value],
    ]
    backwards_diagonal = [
        [Player.x_char.value, Player.none.value, Player.none.value],
        [Player.none.value, Player.x_char.value, Player.none.value],
        [Player.none.value, Player.none.value, Player.x_char.value],
    ]
    forwards_diagonal = [
        [Player.none.value, Player.none.value, Player.x_char.value],
        [Player.none.value, Player.x_char.value, Player.none.value],
        [Player.x_char.value, Player.none.value, Player.none.value],
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
    return {
        0: Player.x_char,
        1: Player.o_char,
        2: Player.x_char,
        3: Player.x_char,
        4: Player.o_char,
        5: Player.x_char,
        6: Player.o_char,
        7: Player.x_char,
        8: Player.o_char,
    }
