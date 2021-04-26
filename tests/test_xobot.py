"""Tests for AI player."""

from typing import List, Tuple

import pytest
from tictactoe.scripts.board import Board
from tictactoe.scripts.mark import Mark
from tictactoe.scripts.xobot import XoBot


def build_game_situations() -> List[Tuple[Board, Tuple[int, int]]]:  # noqa: WPS213 WPS234 E501
    """Build game situations for testing a next move."""
    board_one = Board()
    board_one.make_move((0, 0), Mark.x_char)
    board_one.make_move((0, 1), Mark.o_char)
    board_one.make_move((1, 0), Mark.x_char)
    board_one.make_move((1, 1), Mark.o_char)

    board_two = Board()
    board_two.make_move((0, 0), Mark.x_char)
    board_two.make_move((2, 2), Mark.o_char)
    board_two.make_move((2, 0), Mark.x_char)
    board_two.make_move((1, 2), Mark.o_char)
    board_two.make_move((0, 2), Mark.x_char)
    board_two.make_move((2, 1), Mark.o_char)

    board_three = Board()
    board_three.make_move((0, 1), Mark.x_char)
    board_three.make_move((0, 0), Mark.o_char)
    board_three.make_move((0, 2), Mark.x_char)
    board_three.make_move((1, 1), Mark.o_char)

    board_four = Board()
    board_four.make_move((0, 2), Mark.x_char)
    board_four.make_move((0, 0), Mark.o_char)
    board_four.make_move((2, 0), Mark.x_char)
    board_four.make_move((1, 1), Mark.o_char)
    board_four.make_move((2, 2), Mark.x_char)
    board_four.make_move((2, 1), Mark.o_char)

    return list(
        zip(
            (board_one, board_two, board_three, board_four), ((2, 0), (0, 1), (2, 2), (1, 2)),  # noqa: E501
        ),
    )


@pytest.mark.parametrize('example, expected', build_game_situations())
def test_select_move(example: Board, expected: Tuple[Tuple[int, int]]):
    """Test choosing next move for current player.

    Args:
        example: board state
        expected: coordinate of cell
    """
    x_player = XoBot(Mark.x_char)
    assert x_player.select_move(example) == expected


@pytest.mark.parametrize('example, expected', build_game_situations())
def test_find_best_choice(example: Board, expected: Tuple[Tuple[int, int]]):
    """Test finding the best choice from possible moves on game board.

    Args:
        example: board state
        expected: coordinate of cell
    """
    x_player = XoBot(Mark.x_char)
    assert x_player._find_best_choice(example, x_player.player).move == expected  # noqa: WPS437 E501
