"""Module for Round class."""
import json
import os

import tictactoe.scripts.db as db
from dataclass_factory import Factory
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from tictactoe.scripts.bot_handler import OhMyBot
from tictactoe.scripts.game import Game
from tictactoe.scripts.keyboard import choice
from tictactoe.scripts.mark import Mark

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = OhMyBot(BOT_TOKEN)
server_name = ''

bot.set_webhook('{0}/hook'.format(server_name))

app = FastAPI()


@app.post('/hook')
async def updates_handler(request: Request):
    """Update handler for Telegram requests.

    Args:
        request: request from Telegram webhook
    """
    update = await request.json()
    message = update.get('message')
    callback = update.get('callback_query')

    if message:
        chat_id = message['chat']['id']
        message_id = message['message_id']
        if message.get('text') == '/start':
            user_id = message['from']['id']
            db.check_db_exists()
            db.insert_user(user_id)
            start_flag = db.fetch_start_flag(user_id)
            if start_flag:
                bot.send_sticker(
                    chat_id=chat_id,
                    sticker='CAACAgQAAxkBAAEFg5BgqTQU3436g5_TOTSLgujFYw5b7AACEQADmDVxAkmg3XnDZam0HwQ',  # noqa: E501
                )
                bot.send_message(
                    chat_id=chat_id,
                    message='Choose your destiny, mortal!',
                    keyboard=choice,
                )
                db.switch_start_flag(user_id)
                db.fetch_start_flag(user_id)
        bot.delete_message(chat_id, message_id)

    elif callback:
        callback_data = json.loads(callback['data'])
        chat_id = callback['message']['chat']['id']
        mssg_id = callback['message']['message_id']
        user_id = callback['from']['id']
        if callback_data.get('start'):
            bot.delete_message(chat_id=chat_id, message_id=mssg_id)
            bot.delete_message(chat_id=chat_id, message_id=mssg_id - 1)
            factory = Factory()
            user_player = factory.load(callback_data['player'], Mark)
            game = Game(user_player, bot=bot)
            game.run_turn(chat_id, callback_data)
            db.update_game_state(game, user_id)
        elif callback_data.get('coordinates'):
            game = db.fetch_game_state(user_id)
            game.run_turn(chat_id, callback_data)
            if game.is_over():
                db.update_games_statistic(game, user_id)
                stats_view = db.get_stats_view(user_id, game)
                board_view = game.board.get_view()
                bot.delete_message(chat_id=chat_id, message_id=mssg_id - 1)
                bot.edit_message(
                    chat_id=chat_id,
                    message_id=mssg_id,
                    message='{0}{1}'.format(board_view, stats_view),
                )
                bot.send_sticker(
                    chat_id=chat_id,
                    sticker='CAACAgQAAxkBAAEFosFgviU_9UWjmvFYMKSJPOjVWZ9CXAACGwADmDVxApFTHg4W1PB8HwQ',  # noqa: E501
                )
                bot.send_message(
                    chat_id=chat_id,
                    message='Bite my shiny virtual ass, meatbag!',
                )
                db.switch_start_flag(user_id)
            db.update_game_state(game, user_id)
    return {'ok': 200}
