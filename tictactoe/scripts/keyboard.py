"""Keyboard class module."""
import json
from typing import Dict, List, Optional

from dataclass_factory import Factory
from tictactoe.scripts.board import Board
from tictactoe.scripts.mark import Mark


def create_button(text: str = ' ', **kwargs) -> dict:
    """Create button for inline Telegram keyboard.

    Args:
        text: message text
        kwargs: optional params

    Returns:
        inline keyboard button
    """
    callback_data = json.dumps(kwargs)
    return {'text': text, 'callback_data': callback_data}


def create_keyboard(  # noqa: WPS234
    inline_keyboard: Optional[List[List[Dict]]] = None,
) -> str:
    """Create inline Telegram keyboard.

    Args:
        inline_keyboard: keyboard with buttons

    Returns:
        inline_keyboard in json format
    """
    return json.dumps({'inline_keyboard': inline_keyboard})


factory = Factory()
board = Board()

board_chars = {
    Mark.x_char: '\u274c',
    Mark.o_char: '\u2b55',
    Mark.empty_cell: ' ',
}
grid = board.get_grid()

choice = create_keyboard(
    inline_keyboard=[
        [
            create_button(
                text='\u274c',
                player=factory.dump(Mark.x_char, Mark),
                start=True,
            ),
            create_button(
                text='\u2b55',
                player=factory.dump(Mark.o_char, Mark),
                start=True,
            ),
        ],
    ],
)

keyboard = create_keyboard(
    inline_keyboard=[
        [
            create_button(
                text=board_chars[mark],
                coordinates=(row, col),
            ) for col, mark in enumerate(line)
        ] for row, line in enumerate(grid)
    ],
)
