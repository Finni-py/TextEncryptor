from telebot.types import Message
from telebot import types

from app.messages.message_text import START_TEXT
from app.bot_instance import bot


def start(message: Message) -> None:
    # Обрабатывает команду /start — приветствует пользователя и показывает клавиатуру с кнопками
    nickname = message.from_user.username
    user_name = message.from_user.first_name or "друг"
    print(f'[+] {nickname} запустил бота')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('/encrypt')
    button_2 = types.KeyboardButton('/decrypt')
    markup.add(button_1, button_2)

    bot.send_message(message.chat.id, START_TEXT.format(user_name=user_name), reply_markup=markup)
