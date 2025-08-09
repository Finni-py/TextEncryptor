from telebot.types import Message
from telebot import types

from app.handlers.start_handler import start
from app.bot_instance import bot
from app.handlers.decrypt_handler import decrypt_input_crypt
from app.handlers.encrypt_handler import work_with_input_size
from app.messages.message_text import HELP_TEXT, GITHUB_LINK, ENCRYPT_START_TEXT

commands = [
    types.BotCommand('start', 'Запуск бота'),
    types.BotCommand('encrypt', 'Шифрует сообщение'),
    types.BotCommand('decrypt', 'Расшифровывает сообщение'),
    types.BotCommand('help', 'Список команд'),
    types.BotCommand('github', 'Ссылка на GitHub проекта')
]


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/start'))
def handler_start(message: Message) -> None:
    start(message)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/help'))
def help(message: Message) -> None:
    # Отправляет справочную информацию по командам
    bot.send_message(message.chat.id, HELP_TEXT)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/github'))
def send_my_github(message: Message) -> None:
    # Отправляет ссылку на GitHub проекта
    bot.send_message(message.chat.id, GITHUB_LINK)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/encrypt'))
def encrypt(message: Message) -> None:
    # Запускает процесс шифрования — запрашивает у пользователя уровень сложности
    bot.send_message(message.chat.id, ENCRYPT_START_TEXT)
    bot.register_next_step_handler(message, work_with_input_size)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/decrypt'))
def decrypt(message: Message) -> None:
    # Запускает процесс расшифровки — запрашивает зашифрованный текст
    bot.send_message(message.chat.id, '🔐 Введи зашифрованное сообщение:')
    bot.register_next_step_handler(message, decrypt_input_crypt)


def main():
    # Устанавливает команды бота и запускает его опрос Telegram API
    bot.set_my_commands(commands)
    bot.polling(none_stop=True)
