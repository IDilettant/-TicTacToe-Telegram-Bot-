"""Module of Game class."""
import random

from tictactoe.scripts.board import Board
from tictactoe.scripts.mark import Mark
from tictactoe.scripts.xobot import XoBot


class Game:
    """Game process class."""

    def __init__(self, user_player: Mark):
        """Initialize a class instance.

        Args:
            user_player: human player char
        """
        self.board = Board()
        self.user_player = user_player
        self.bot = XoBot(user_player.switch_char())
        self.current_player = Mark.x_char

    def run_round(self):
        """Run round of game."""
        self._show_board()
        if self.bot.player == Mark.x_char:
            move = random.choice(
                ((0, 0), (0, 2), (2, 0), (2, 2)),
            )
            self.board.make_move(move, self.bot.player)
            self._switch_turn()
            self._show_board()

        while self.board.legal_moves:
            self.make_current_player_move()
            self._switch_turn()
            self._show_board()
            if self.board.has_win():
                break
        print('You can never win, leather bastard!')

    def make_current_player_move(self):
        """Make move for current player turn."""
        if self.current_player == self.bot.player:
            self._make_bot_move()
        else:
            self.make_user_move()

    def make_user_move(self):
        """Make move for user turn."""
        move = None
        while move not in self.board.legal_moves:
            print('Enter legal coordinates')
            move = (
                int(input('Select row number: ')),
                int(input('Select column number: ')),
            )
        self.board.make_move(move, self.user_player)

    def _make_bot_move(self):
        move = self.bot.select_move(self.board)
        self.board.make_move(move, self.bot.player)

    def _switch_turn(self):
        self.current_player = self.current_player.switch_char()

    def _show_board(self):
        grid = self.board.get_grid()
        for line in grid:
            print(*line)
        print()
