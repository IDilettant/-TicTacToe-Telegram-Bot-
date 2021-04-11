"""Basic module for bot logic."""
import copy
from sys import maxsize

from tictactoe.scripts.player import Player


class Node(object):
    """Node of tree of possible states of game board."""

    def __init__(self, move=0, value=0, depth=0):  # noqa: WPS110
        """Build a class instance.

        Args:
            move (int): coordinate of board cell
            value (int): outcome significance of board state
            depth (int): sequential number of the tree level
        """
        self.move = move
        self.value = value  # noqa: WPS110
        self.depth = depth


class XoBot(object):
    """A bot for tic tac toe game.

    implements the minimax algorithm with alpha-beta pruning
    and depth-first search strategy
    """

    def __init__(self, player):
        """Build a class constructor.

        Args:
            player: selected player for bot
        """
        self.player = player

    def _make_alpha_pruning(
        self,
        node,
        alpha_choice,
        beta_choice,
    ):
        """Make branch pruning for maximizing player.

        Args:
            node: node of tree of possible choices of game board state
            alpha_choice: class instance containing value of upper bound
            beta_choice: class instance containing value of lower bound

        Returns:
            Class instance contain value for upper bound of possible solutions
        """
        if node.value > alpha_choice.value:
            alpha_choice = node
        if alpha_choice.value >= beta_choice.value:
            return node
        return alpha_choice

    def _make_beta_pruning(
        self,
        node,
        alpha_choice,
        beta_choice,
    ):
        """Make branch pruning for minimizing player.

        Args:
            node: node of tree of possible choices of game board state
            alpha_choice: class instance containing value of upper bound
            beta_choice: class instance containing value of lower bound

        Returns:
            Class instance contain value for lower bound of possible solutions
        """
        if node.value < beta_choice.value:
            beta_choice.value = node.value
        if alpha_choice.value >= beta_choice.value:
            return node
        return beta_choice

    def _make_deep_first_search(  # noqa: WPS211 WPS210
        self,
        board,
        current_player,
        depth,
        alpha_choice,
        beta_choice,
    ):
        """Search best move for possible moves on game board.

        Args:
            board: current state of game board
            current_player: a player which make the current move
            depth (int): sequential number of the tree level
            alpha_choice: class instance containing value of upper bound
            beta_choice: class instance containing value of lower bound

        Returns:
            Class instance containing best possible move
        """
        legal_moves = board.get_legal_moves()
        for move in legal_moves:
            new_board = copy.deepcopy(board)
            new_board.make_move(move, current_player)
            node = self._find_best_choice(
                new_board,
                current_player.switch_turn(),
                depth + 1,
                alpha_choice.value,
                beta_choice.value,
            )
            node.move = new_board.last_move
            if current_player == Player.x_char:
                alpha_choice = self._make_alpha_pruning(
                    node, alpha_choice, beta_choice,
                )
            else:
                beta_choice = self._make_beta_pruning(
                    node, alpha_choice, beta_choice,
                )
        return alpha_choice if current_player == Player.x_char else beta_choice

    def _find_best_choice(  # noqa: WPS211
        self,
        board,
        current_player,
        depth=0,
        alpha=-maxsize,
        beta=maxsize,
    ):
        """Find best choice from possible moves on game board.

        Args:
            board: current state of game board
            current_player: a player which make the current move
            depth (int): sequential number of the tree level
            alpha (int): the maximum lower bound of possible solutions
            beta (int): the minimum upper bound of possible solutions

        Returns:
            An instance of Choice class
        """
        alpha_choice = Node(value=alpha)
        beta_choice = Node(value=beta)

        if board.has_win():
            if current_player == Player.x_char:
                return Node(board.get_last_move(), 10 - depth, depth)
            return Node(board.get_last_move(), -10 + depth, depth)
        elif len(board.moves_made) == 9:
            return Node(board.last_move(), 0, depth)

        return self._make_deep_first_search(
            board,
            current_player,
            depth,
            alpha_choice,
            beta_choice,
        )
