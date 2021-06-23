"""Tests for game module."""
import os
from typing import Dict

import pook
from dataclass_factory import Factory
from dotenv import load_dotenv
from tictactoe.scripts.bot_handler import OhMyBot
from tictactoe.scripts.game import Game
from tictactoe.scripts.mark import Mark

load_dotenv()


def test_game():  # noqa: WPS210 WPS218
    """Test to module helper functions."""
    ai_bot = OhMyBot('some token')
    factory = Factory()
    game = Game(Mark.o_char, ai_bot)
    assert game.current_player == game.AI.player
    callback_data = {
        'player': factory.dump(Mark.o_char, Mark), 'coordinates': (1, 1),
    }
    game._make_bot_move()  # noqa: WPS437, move = (0, 0)
    assert game.board.current_state[game.board.last_move] == Mark.x_char
    game._switch_turn()  # noqa: WPS437
    assert game.current_player == Mark.o_char
    game.make_user_move(callback_data)
    assert game.board.current_state[game.board.last_move] == Mark.o_char
    assert game.board.last_move == callback_data['coordinates']
    callback_data = {
        'player': factory.dump(Mark.o_char, Mark), 'coordinates': (0, 2),
    }
    move = callback_data['coordinates']
    player = factory.load(callback_data['player'], Mark)
    game.make_user_move(callback_data)
    assert game.board.current_state[move] == player
    assert game.board.last_move == move


def test_is_over_tie_state(tie_state: Dict):
    """Test end-of-game confirmation in case of a draw.

    Args:
        tie_state: tie state of game board
    """
    ai_bot = OhMyBot('some token')
    game = Game(Mark.o_char, ai_bot)
    game.board.current_state = tie_state
    assert game.is_over()


@pook.on
def test_run_turn():  # noqa: WPS210 WPS218
    """Test main function of module."""
    bot_token = os.getenv('BOT_TOKEN')
    api_url = 'https://api.telegram.org/bot{0}/'.format(bot_token)
    factory = Factory()
    move = (1, 1)
    callback_data = {
        'player': factory.dump(Mark.o_char, Mark), 'coordinates': move,
    }
    start_callback_data = {'start': True}
    reply = 200
    response_json = {'result': {'message_id': 99}}
    chat_id = 66
    pook.post(
        '{0}sendSticker'.format(api_url),
        reply=reply,
        response_json=response_json,
    )
    pook.post(
        '{0}sendMessage'.format(api_url),
        reply=reply,
        response_json=response_json,
    )
    pook.post(
        '{0}editMessageText'.format(api_url),
        times=2,
        reply=reply,
        response_json=response_json,
    )
    bot = OhMyBot(bot_token)
    game = Game(user_player=Mark.o_char, bot=bot)
    game.run_turn(chat_id=chat_id, callback_data=start_callback_data)
    assert game.update == response_json
    assert game.board.moves_made
    assert game.board.current_state[game.board.last_move] == game.AI.player
    assert game.current_player == game.user_player
    game.run_turn(chat_id=chat_id, callback_data=callback_data)
    assert game.current_player == game.user_player
    assert game.board.current_state[game.board.last_move] == game.AI.player
    assert game.board.current_state[move] == game.user_player
