"""Request handler to Telegram API."""
from typing import Optional

import requests


class OhMyBot:
    """Request handler to Telegram API."""

    def __init__(self, token: str):
        """Initialize a class instance.

        Args:
            token: bot token
        """
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{0}/'.format(self.token)

    def send_message(
        self,
        chat_id: int,
        message: str,
        keyboard: Optional[str] = None,
    ) -> str:
        """Send message to chat.

        Args:
            chat_id: id of chat with user
            message: text of message
            keyboard: game board

        Returns:
            http response
        """
        payload = {
            'chat_id': chat_id,
            'text': message,
            'reply_markup': keyboard,
        }
        method = 'sendMessage'
        method_url = '{0}{1}'.format(self.api_url, method)
        response = requests.post(method_url, data=payload)
        response.raise_for_status()
        return response.json()

    def edit_message(
        self,
        chat_id: int,
        message_id: int,
        message: str,
        keyboard: Optional[str] = None,
    ) -> str:
        """Edit message in chat.

        Args:
            chat_id: id of chat with user
            message_id: id of message in chat with user
            message: text of message
            keyboard: game board

        Returns:
            http response
        """
        payload = {
            'message_id': message_id,
            'chat_id': chat_id,
            'text': message,
            'reply_markup': keyboard,
        }
        method = 'editMessageText'
        method_url = '{0}{1}'.format(self.api_url, method)
        response = requests.post(method_url, data=payload)
        response.raise_for_status()
        return response.json()

    def delete_message(self, chat_id: int, message_id: int) -> str:
        """Delete message from chat.

        Args:
            chat_id: id of chat with user
            message_id: id of message in chat with user

        Returns:
            http response
        """
        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
        }
        method = 'deleteMessage'
        method_url = '{0}{1}'.format(self.api_url, method)
        response = requests.post(method_url, data=payload)
        response.raise_for_status()
        return response.json()

    def send_sticker(
        self,
        chat_id: int,
        sticker: str,
        reply_markup: Optional[str] = None,
    ) -> str:
        """Send sticker to chat.

        Args:
            chat_id: id of chat with user
            sticker: Telegram sticker code
            reply_markup: inline keyboard for game board

        Returns:
            http response
        """
        payload = {
            'chat_id': chat_id,
            'sticker': sticker,
            'reply_markup': reply_markup,
        }
        method = 'sendSticker'
        method_url = '{0}{1}'.format(self.api_url, method)
        response = requests.post(method_url, data=payload)
        response.raise_for_status()
        return response.json()

    def set_webhook(self, server_url) -> str:
        """Set webhook for getting updates.

        Args:
            server_url: server url with app

        Returns:
            http response
        """
        payload = {'url': server_url}
        method = 'setWebhook'
        method_url = '{0}{1}'.format(self.api_url, method)
        response = requests.get(method_url, params=payload)
        response.raise_for_status()
        return response.json()

    def remove_webhook(self):
        """Remove webhook for server app."""
        return self.set_webhook('')
