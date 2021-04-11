"""Basic module for bot logic."""


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
