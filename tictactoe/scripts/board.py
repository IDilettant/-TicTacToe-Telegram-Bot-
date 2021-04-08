"""Board module."""


class Board(object):
    """Game board class."""

    def __init__(self):
        """Build a class constructor.

        The constructor takes the side size,
        the basic state of the board and a list of moves
        """
        self.side_size = 3
        self.current_state = {
            cell: ' . ' for cell in range(self.side_size ** 2)
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
                self.current_state[keys.pop(0)] for _ in range(self.side_size)
            ] for _ in range(self.side_size)
        ]

    def make_move(self, move, player_char):
        """Change board current state based on the move made.

        Args:
            move (int): coordinate of board cell
            player_char (str): char of current player

        Returns:
            Board current state
        """
        legal_moves = [
            cell for cell, char in self.current_state.items() if char == ' . '
        ]
        if move in legal_moves:
            self.current_state[move] = player_char
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
