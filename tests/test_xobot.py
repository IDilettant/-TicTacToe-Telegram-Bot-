"""Tests for AI player."""

import pytest
from tictactoe.scripts.board import Board
from tictactoe.scripts.player import Player
from tictactoe.scripts.xobot import Node, XoBot


def build_game_situations():  # noqa: WPS213
    """Build game situations for testing a next move.

    Returns:
        board states
    """
    board_one = Board()
    board_one.make_move(4, Player.x_char)
    board_one.make_move(1, Player.o_char)
    board_one.make_move(3, Player.x_char)
    board_one.make_move(0, Player.o_char)

    board_two = Board()
    board_two.make_move(4, Player.x_char)
    board_two.make_move(5, Player.o_char)
    board_two.make_move(0, Player.x_char)
    board_two.make_move(8, Player.o_char)
    board_two.make_move(2, Player.x_char)
    board_two.make_move(7, Player.o_char)

    board_three = Board()
    board_three.make_move(2, Player.x_char)
    board_three.make_move(4, Player.o_char)
    board_three.make_move(1, Player.x_char)
    board_three.make_move(0, Player.o_char)

    board_four = Board()
    board_four.make_move(8, Player.x_char)
    board_four.make_move(4, Player.o_char)
    board_four.make_move(1, Player.x_char)
    board_four.make_move(0, Player.o_char)
    board_four.make_move(3, Player.x_char)
    board_four.make_move(6, Player.o_char)

    return list(
        zip((board_one, board_two, board_three, board_four), (5, 1, 8, 2)),
    )


@pytest.mark.parametrize('example, expected', build_game_situations())
def test_select_move(example: Board, expected: int):
    """Test choosing next move for current player.

    Args:
        example: board state
        expected: coordinate of cell
    """
    x_player = XoBot(Player.x_char)
    assert x_player.select_move(example) == expected


def test_make_alpha_pruning():  # noqa: WPS210
    """Test branch pruning for maximizing player."""
    bot = XoBot(Player.x_char)

    # alpha > beta, alpha < node
    node_one = Node(value=3)  # noqa: WPS204
    alpha_choice_one = Node(value=2)  # noqa: WPS204
    beta_choice_one = Node(value=1)  # noqa: WPS204

    # alpha < beta, alpha < node
    node_two = Node(value=2)
    alpha_choice_two = Node(value=1)
    beta_choice_two = Node(value=3)

    # alpha > beta, alpha > node
    node_three = Node(value=1)
    alpha_choice_three = Node(value=3)
    beta_choice_three = Node(value=2)

    # alpha < beta, alpha > node
    node_four = Node(value=1)
    alpha_choice_four = Node(value=2)
    beta_choice_four = Node(value=3)

    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_one,
        alpha_choice=alpha_choice_one,
        beta_choice=beta_choice_one,
    ) is node_one
    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_two,
        alpha_choice=alpha_choice_two,
        beta_choice=beta_choice_two,
    ) is node_two
    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_three,
        alpha_choice=alpha_choice_three,
        beta_choice=beta_choice_three,
    ) is node_three
    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_four,
        alpha_choice=alpha_choice_four,
        beta_choice=beta_choice_four,
    ) is alpha_choice_four


def test_make_beta_pruning():  # noqa: WPS210
    """Test branch pruning for minimizing player."""
    bot = XoBot(Player.x_char)

    # beta < alpha, beta > node
    node_one = Node(value=1)
    alpha_choice_one = Node(value=3)  # noqa: WPS204
    beta_choice_one = Node(value=2)  # noqa: WPS204

    # beta < alpha, beta < node
    node_two = Node(value=2)
    alpha_choice_two = Node(value=2)
    beta_choice_two = Node(value=1)

    # beta > alpha, beta < node
    node_three = Node(value=3)
    alpha_choice_three = Node(value=1)
    beta_choice_three = Node(value=2)

    # beta > alpha, beta > node
    node_four = Node(value=1)
    alpha_choice_four = Node(value=2)
    beta_choice_four = Node(value=3)

    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_one,
        alpha_choice=alpha_choice_one,
        beta_choice=beta_choice_one,
    ) is node_one
    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_two,
        alpha_choice=alpha_choice_two,
        beta_choice=beta_choice_two,
    ) is node_two
    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_three,
        alpha_choice=alpha_choice_three,
        beta_choice=beta_choice_three,
    ) is node_three
    assert bot._make_alpha_pruning(  # noqa: WPS437
        node=node_four,
        alpha_choice=alpha_choice_four,
        beta_choice=beta_choice_four,
    ) is alpha_choice_four


def test_make_deep_first_search():
    pass


def test_find_best_choice():
    pass
