"""Module of Game class."""
import random
from typing import Dict, Optional

from dataclass_factory import Factory
from tictactoe.scripts.board import Board
from tictactoe.scripts.bot_handler import OhMyBot
from tictactoe.scripts.keyboard import create_button, create_keyboard
from tictactoe.scripts.mark import Mark
from tictactoe.scripts.xobot import XoBot


class Game:
    """Game process class."""

    def __init__(self, user_player: Mark, bot: OhMyBot):
        """Initialize a class instance.

        Args:
            user_player: human player char
            bot: request handler to Telegram API
        """
        self.board: Board = Board()
        self.user_player: Mark = user_player
        self.AI: XoBot = XoBot(user_player.switch_char())
        self.current_player: Mark = Mark.x_char
        self.bot: OhMyBot = bot
        self.update: Optional[dict] = None

    def run_turn(self, chat_id: int, callback_data: Dict):  # noqa: WPS213
        """Run round of game.

        Args:
            chat_id: id number of chat
            callback_data: callback data from inline keyboard
        """
        if callback_data.get('coordinates'):
            move = tuple(callback_data['coordinates'])
            if move in self.board.legal_moves:
                self.make_user_move(callback_data)
                self._switch_turn()
                self._make_bot_move()
                self._switch_turn()
                self.show_game_board(chat_id)

        else:
            self.show_game_board(chat_id)
            if self.AI.player == Mark.x_char:
                move = random.choice(
                    ((0, 0), (0, 2), (2, 0), (2, 2)),  # optimizing heuristic
                )
                self.board.make_move(move, self.AI.player)
                self._switch_turn()
                self.show_game_board(chat_id)

    def make_user_move(self, callback_data: Dict):
        """Make move for user turn.

        Args:
            callback_data: callback data from inline keyboard
        """
        move = tuple(callback_data['coordinates'])
        if move in self.board.legal_moves:
            self.board.make_move(move, self.user_player)

    def show_game_board(self, chat_id: int):  # noqa: WPS210
        """Show current game board in chat.

        Args:
            chat_id: id number of chat
        """
        board_chars = {
            Mark.x_char: '\u274c',
            Mark.o_char: '\u2b55',
            Mark.empty_cell: ' ',
        }
        grid = self.board.get_grid()
        factory = Factory()
        keyboard = create_keyboard(
            inline_keyboard=[
                [
                    create_button(
                        text=board_chars[mark],
                        player=factory.dump(mark, Mark),
                        coordinates=(row, col),
                    ) for col, mark in enumerate(line)
                ] for row, line in enumerate(grid)
            ],
        )
        if self.board.moves_made:
            message_id = self.update['result']['message_id']
            self.bot.edit_message(
                chat_id=chat_id,
                message_id=message_id,
                message='Show me what you can!',
                keyboard=keyboard,
            )
        else:
            self.bot.send_sticker(
                chat_id=chat_id,
                sticker='CAACAgQAAxkBAAEFg5xgqT9fQq0zAWm4s24nNhPA2f2JOAACEwADmDVxAp3k1xTFyNcyHwQ',  # noqa: E501
            )
            self.update = self.bot.send_message(
                chat_id=chat_id,
                message='Show me what you can!',
                keyboard=keyboard,
            )

    def is_over(self):
        """Check game completion.

        Returns:
            bool
        """
        return self.board.has_win() or not self.board.legal_moves

    def _make_bot_move(self):
        move = self.AI.select_move(self.board)
        self.board.make_move(move, self.AI.player)

    def _switch_turn(self):
        self.current_player = self.current_player.switch_char()
