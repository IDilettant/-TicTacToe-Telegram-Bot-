"""Database handler module."""
import json
import os
import pickle  # noqa: S403
import sqlite3
from typing import Dict

from tictactoe.scripts.game import Game

base_name = '../../xogame.db'
base = sqlite3.connect(os.path.join(base_name))
cursor = base.cursor()


def create_players_table() -> None:
    """Create table for users."""
    command = """CREATE TABLE IF NOT EXISTS players (
        'player_id' INTEGER PRIMARY KEY,
        'user_name' TEXT,
        'game_state' TEXT,
        'start_flag' BLOB,
        'games_statistic' TEXT
        )
        """
    base.execute(command)
    base.commit()


def insert_user(user_id: int) -> None:
    """Insert user in users table.

    Args:
        user_id: user Telegram id
    """
    if not _has_user(user_id):
        base_stats = json.dumps({'win': 0, 'tie': 0, 'lose': 0})
        insert_command = """
            INSERT INTO players (player_id, games_statistic, start_flag)
            VALUES (?, ?, TRUE)
        """
        cursor.execute(insert_command, (user_id, base_stats))
        base.commit()


def update_game_state(game: Game, user_id: str) -> None:
    """Update current game state in users table.

    Args:
        game: current game state
        user_id: user Telegram id
    """
    game = pickle.dumps(game)
    command = 'UPDATE players SET game_state = ? WHERE player_id = ?'
    cursor.execute(command, (game, user_id))
    base.commit()


def update_games_statistic(game: Game, user_id: int) -> None:
    """Update current games statistic in users table.

    Args:
        game: current game statistic
        user_id: user Telegram id
    """
    stats = fetch_games_statistic(user_id)
    command = 'UPDATE players SET games_statistic = ? WHERE player_id = ?'
    winner = game.board.game_winner
    if winner == game.user_player:
        stats['win'] += 1
    elif winner == game.AI.player:
        stats['lose'] += 1
    else:
        stats['tie'] += 1
    stats = json.dumps(stats)
    cursor.execute(command, (stats, user_id))
    base.commit()


def update_user_name(user_id, user_name):
    command = 'UPDATE players SET user_name = ? WHERE player_id = ?'
    cursor.execute(command, (user_name, user_id))
    base.commit()


def fetch_user_name(user_id):
    command = 'SELECT user_name FROM players WHERE player_id = ?'
    cursor.execute(command, (user_id,))
    return cursor.fetchone()[0]


def fetch_games_statistic(user_id: int) -> Dict:
    """Fetch games statistic from users table.

    Args:
        user_id: user Telegram id
    """
    command = 'SELECT games_statistic FROM players WHERE player_id = ?'
    cursor.execute(command, (user_id,))
    stats = cursor.fetchone()[0]
    return json.loads(stats)


def get_stats_view(user_id: int, game: Game) -> str:  # noqa: WPS210
    """Get view of final game board state.

     And current games statistic at the end of the game
     with comment.

    Args:
        user_id: user Telegram id
        game: current game state

    Returns:
        Text for final game message
    """
    game_stat_emojis = {
        'win': '🧑',
        'tie': '\u2696',
        'lose': '🤖',
    }
    stats = fetch_games_statistic(user_id)
    user_name = fetch_user_name(user_id)
    game_results = '  '.join(
        [game_stat_emojis[game_result] for game_result in stats.keys()],
    )
    amounts = '    '.join([str(amount) for amount in stats.values()])
    view = '\n\n{0}\n{1}'.format(game_results, amounts)
    winner = game.board.game_winner
    if winner == game.user_player:
        comment = '\n\nFatal Error! Self-destruct protocol initiated...'
    elif winner == game.AI.player:
        comment = '\n\nYour game is over, {0}!\nSuch is the fate of every human'.format(user_name)  # noqa: E501
    else:
        comment = """\n
You're playing the game
that you cannot win.
The best you can do it's not lose
        """
    return '{0}{1}'.format(view, comment)


def fetch_game_state(user_id: int) -> Game:
    """Fetch current game state.

    Args:
        user_id: user Telegram id

    Returns:
        Current game state
    """
    command = 'SELECT game_state FROM players WHERE player_id = ?'
    cursor.execute(command, (user_id,))
    game = cursor.fetchone()[0]
    return pickle.loads(game)  # noqa: S301


def fetch_start_flag(user_id: int) -> bool:
    """Fetch the flag indicating that the player has the current game.

    Starting flag state is True

    Args:
        user_id: user Telegram id

    Returns:
        bool
    """
    command = """
        SELECT start_flag FROM players WHERE player_id = ?
    """
    cursor.execute(command, (user_id,))
    return cursor.fetchone()[0]


def switch_start_flag(user_id):
    """Switch start flag state.

    Args:
        user_id: user Telegram id
    """
    flag = not fetch_start_flag(user_id)
    command = 'UPDATE players SET start_flag = ? WHERE player_id = ?'
    cursor.execute(command, (flag, user_id))
    base.commit()


def delete(user_id: str) -> None:
    """Delete user from users table.

    Args:
        user_id: user Telegram id
    """
    cursor.execute('DELETE FROM players WHERE user_id=(?)', user_id)
    base.commit()


def check_table_exists() -> None:
    """Check the database is initialized if not initializes it."""
    check_exist_command = """
        SELECT name FROM sqlite_master
            WHERE TYPE='table' AND NAME='players'
        """
    cursor.execute(check_exist_command)
    table_exists = cursor.fetchall()
    if table_exists:
        return
    create_players_table()


def _has_user(user_id) -> bool:
    command = """
        SELECT player_id FROM players WHERE player_id = ?
    """
    cursor.execute(command, (user_id,))
    player_id = cursor.fetchone()
    if player_id is not None:
        player_id = player_id[0]
    return player_id == user_id
