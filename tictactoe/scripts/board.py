"""Board module."""
from tictactoe.scripts.player import Player


class Board(object):
    """Game board class."""

    def __init__(self):
        """Build a class constructor.

        The constructor takes the side size,
        the basic state of the board and a list of moves
        """
        self.side_size = 3
        self.current_state = {
            cell: Player.none for cell in range(self.side_size ** 2)
        }
        self.moves_made = []

    def get_grid(self):
        """Get a grid with chars according the current state of game board.

        Returns:
            Board grid
        """
        keys = list(self.current_state.keys())
        return [
            [
                self.current_state[
                    keys.pop(0)
                ].value for _ in range(self.side_size)
            ] for _ in range(self.side_size)
        ]

    def get_legal_moves(self):
        """Get possible moves for current board state.

        Returns:
            Coordinates of possible moves
        """
        return [
            cell for cell, player in self.current_state.items() if
            player == Player.none
        ]

    def last_move(self):
        """Get the last made move.

        Returns:
            The last made move
        """
        return self.moves_made[-1]

    def make_move(self, move, current_player):
        """Change board current state based on the move made.

        Args:
            move (int): num of board cell
            current_player: a player which make the current move

        Returns:
            Board current state
        """
        legal_moves = self.get_legal_moves()
        if move in legal_moves:
            self.current_state[move] = current_player
        self.moves_made.append(move)
        return self.current_state

    def has_win(self):
        """Check for the win.

        Returns:
            bool
        """
        grid = self.get_grid()
        backwards_diag = [grid[cell][cell] for cell in range(self.side_size)]
        reversed_grid = list(reversed(grid))
        forwards_diag = [
            reversed_grid[cell][cell] for cell in range(self.side_size)
        ]
        if any(map(self._line_has_match, grid)):
            return True
        elif any(map(self._line_has_match, zip(*grid))):
            return True
        elif self._line_has_match(backwards_diag):
            return True
        elif self._line_has_match(forwards_diag):
            return True
        return False

    def _line_has_match(self, line):
        line = set(line)
        return len(line) == 1 and line.pop() != ' . '
