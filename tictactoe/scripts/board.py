"""Board module."""
from typing import List, Tuple, Union

from tictactoe.scripts.mark import Mark


class Board:  # noqa: WPS214
    """Game board class."""

    def __init__(self):
        """Initialize a class instance."""
        self.side_size = 3
        self.current_state = dict.fromkeys(
            [(row, col) for row in range(self.side_size) for col in range(self.side_size)],  # noqa: E501
            Mark.empty_cell,
        )
        self.moves_made = []

    def get_grid(self) -> List[list]:
        """Get a grid with chars according the current state of game board."""
        grid = [list(range(self.side_size)) for _ in range(self.side_size)]
        for cell, mark in self.current_state.items():
            row, col = cell
            grid[row][col] = mark.value
        return grid

    @property
    def legal_moves(self) -> list:
        """Get possible moves for current board state."""
        return [
            cell for cell, mark in self.current_state.items() if
            mark == Mark.empty_cell
        ]

    @property
    def last_move(self) -> Tuple[int, int]:
        """Get the last made move."""
        return self.moves_made[-1]

    @property
    def game_winner(self):
        """Get the game winner char."""
        return self.current_state[self.last_move]

    def make_move(self, move: Tuple[int, int], current_player: Mark) -> dict:
        """Change board current state based on the move made.

        Args:
            move: coordinate of board cell
            current_player: a player that make the current move
        """
        if move in self.legal_moves:
            self.current_state[move] = current_player
        self.moves_made.append(move)
        return self.current_state

    def has_win(self) -> bool:
        """Check for the win."""
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

    def _line_has_match(self, line: Union[list, tuple]) -> bool:
        line = set(line)
        return len(line) == 1 and line.pop() != Mark.empty_cell.value
