import telebot
from telebot.types import Message

from config import API_KEY
from text_fot_bot import *

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'START'])
def start(message: Message) -> None:
    user_name = message.from_user.first_name or "друг"
    bot.send_message(message.chat.id, start_text.format(user_name=user_name))


@bot.message_handler(commands=['help', 'HELP'])
def help(message: Message) -> None:
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['github', 'GITHUB'])
def send_my_github(message: Message) -> None:
    # Отправляет ссылку на GitHub проекта
    bot.send_message(message.chat.id, github_link_text)


bot.polling(non_stop=True)
