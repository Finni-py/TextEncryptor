import telebot
from telebot.types import Message
from telebot import types

from config import API_KEY
from text_fot_bot import *
from custom_encryption import get_random_funcs
from fernet_encryption import get_encrypt_text_fernet

bot = telebot.TeleBot(API_KEY)
commands = [
    types.BotCommand('start', 'Запуск бота'),
    types.BotCommand('encrypt', 'Шифрует сообщение'),
    types.BotCommand('decrypt', 'Расшифровывает сообщение'),
    types.BotCommand('help', 'Список команд'),
    types.BotCommand('github', 'Ссылка на GitHub проекта')
]


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/start'))
def start(message: Message) -> None:
    # Обработка команды /start — отправка приветствия и отображение кнопок
    nickname = message.from_user.username
    user_name = message.from_user.first_name or "друг"
    print(f'[+] {nickname} запустил бота')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton('/encrypt')
    button_2 = types.KeyboardButton('/decrypt')
    markup.add(button_1, button_2)

    bot.send_message(message.chat.id, start_text.format(user_name=user_name), reply_markup=markup)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/help'))
def help(message: Message) -> None:
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/github'))
def send_my_github(message: Message) -> None:
    # Отправляет ссылку на GitHub проекта
    bot.send_message(message.chat.id, github_link_text)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/encrypt'))
def encrypt(message: Message) -> None:
    bot.send_message(message.chat.id, encrypt_start_text)
    bot.register_next_step_handler(message, text_input_size)


def text_input_size(message: Message) -> None:
    try:
        size = int(message.text)
        if 1 <= size <= 3:
            bot.send_message(message.chat.id, encrypt_second_text)
            bot.register_next_step_handler(message, encrypt_input_info, size)
        else:
            raise ValueError
    except ValueError:
        bot.send_message(message.chat.id, '❗️Неверный уровень сложности. Введите 1, 2 или 3')
        bot.register_next_step_handler(message, text_input_size)


def encrypt_input_info(message: Message, size: int = 2) -> None:
    encrypt_text_fernet, key_fernet = get_encrypt_text_fernet(message.text)
    encrypt_text_custom, key_custom = get_random_funcs((encrypt_text_fernet, key_fernet), size)
    bot.send_message(
        message.chat.id,
        f"🔐 Зашифрованный текст\n {encrypt_text_custom}\n\n🗝 Ключ\n {key_custom}\n\n"
        "⚠️ Не показывай данные никому!"
    )


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/decrypt'))
def decrypt(message: Message) -> None:
    bot.send_message(message.chat.id, 'Функция еще не готова!')


def main():
    bot.set_my_commands(commands)
    bot.polling(none_stop=True)
