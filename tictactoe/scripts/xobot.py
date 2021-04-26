"""AI-player logic."""
import copy
from dataclasses import dataclass
from sys import maxsize
from typing import Optional, Tuple

from tictactoe.scripts.board import Board
from tictactoe.scripts.mark import Mark


@dataclass
class Node:
    """Node of tree of possible states of game board."""

    move: Optional[Tuple[int, int]] = None
    value: int = 0  # noqa: WPS110


class XoBot:
    """A bot for tic tac toe game.

    Implements the minimax algorithm with alpha-beta pruning
    and depth-first search strategy
    link: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    """

    def __init__(self, player: Mark):
        """Initialize a class instance.

        Args:
            player: selected player for bot
        """
        self.player = player

    def select_move(self, board: Board) -> Optional[Tuple[int, int]]:
        """Choose next move for current player.

        Args:
            board: current state of game board
        """
        node = self._find_best_choice(board, self.player)
        return node.move

    def _find_best_choice(  # noqa: WPS211
        self,
        board: Board,
        current_player: Mark,
        depth: int = 0,
        alpha: int = -maxsize,
        beta: int = maxsize,
    ) -> Node:
        """Find best choice from possible moves on game board.

        Args:
            board: current state of game board
            current_player: a player which make the current move
            depth: sequential number of the tree level
            alpha: the maximum lower bound of possible solutions
            beta: the minimum upper bound of possible solutions
        """
        alpha_choice = Node(value=alpha)
        beta_choice = Node(value=beta)

        if board.has_win():
            if board.game_winner == Mark.x_char:
                return Node(
                    move=board.last_move,
                    value=((board.side_size ** 2 + 1) - depth),
                )
            return Node(
                move=board.last_move,
                value=(-(board.side_size ** 2 + 1) + depth),
            )
        elif len(board.moves_made) == board.side_size ** 2:
            return Node(move=board.last_move, value=0)

        return self._make_deep_first_search(
            board,
            current_player,
            depth,
            alpha_choice,
            beta_choice,
        )

    def _make_deep_first_search(  # noqa: WPS211 WPS210
        self,
        board: Board,
        current_player: Mark,
        depth: int,
        alpha_choice: Node,
        beta_choice: Node,
    ) -> Node:
        """Search best move for possible moves on game board.

        Args:
            board: current state of game board
            current_player: a player which make the current move
            depth: sequential number of the tree level
            alpha_choice: class instance containing value of upper bound
            beta_choice: class instance containing value of lower bound
        """
        for move in board.legal_moves:
            new_board = copy.deepcopy(board)
            new_board.make_move(move, current_player)
            node = self._find_best_choice(
                new_board,
                current_player.switch_char(),
                depth + 1,
                alpha_choice.value,
                beta_choice.value,
            )
            node.move = new_board.last_move
            alpha_choice, beta_choice = self._update_alpha_beta(
                current_player,
                node,
                alpha_choice,
                beta_choice,
            )
            # alpha-beta pruning
            if alpha_choice.value >= beta_choice.value:
                return node
        return alpha_choice if current_player == Mark.x_char else beta_choice

    def _update_alpha_beta(
        self,
        current_player: Mark,
        node: Node,
        alpha_choice: Node,
        beta_choice: Node,
    ) -> Tuple[Node, Node]:
        if current_player == Mark.x_char:
            if node.value > alpha_choice.value:
                alpha_choice = node
        else:
            if node.value < beta_choice.value:  # noqa: WPS513
                beta_choice = node
        return alpha_choice, beta_choice
