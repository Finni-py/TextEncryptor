import telebot
from telebot.types import Message
from telebot import types

from app.config import API_KEY
from app.text_fot_bot import *
from app.custom_decryption import get_stock_crypt
from app.custom_encryption import get_random_funcs
from app.fernet_encryption import get_encrypt_text_fernet, get_decrypt_text_fernet

bot = telebot.TeleBot(API_KEY)
commands = [
    types.BotCommand('start', 'Запуск бота'),  # Команда /start
    types.BotCommand('encrypt', 'Шифрует сообщение'),  # Команда /encrypt
    types.BotCommand('decrypt', 'Расшифровывает сообщение'),  # Команда /decrypt
    types.BotCommand('help', 'Список команд'),  # Команда /help
    types.BotCommand('github', 'Ссылка на GitHub проекта')  # Команда /github
]


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/start'))
def start(message: Message) -> None:
    # Обрабатывает команду /start — приветствует пользователя и показывает клавиатуру с кнопками
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
    # Отправляет справочную информацию по командам
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/github'))
def send_my_github(message: Message) -> None:
    # Отправляет ссылку на GitHub проекта
    bot.send_message(message.chat.id, github_link_text)


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/encrypt'))
def encrypt(message: Message) -> None:
    # Запускает процесс шифрования — запрашивает у пользователя уровень сложности
    bot.send_message(message.chat.id, encrypt_start_text)
    bot.register_next_step_handler(message, text_input_size)


def text_input_size(message: Message) -> None:
    # Получает уровень сложности от пользователя, проверяет его и просит ввести текст для шифрования
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
    # Получает текст для шифрования, шифрует его двумя методами (fernet и кастомным), и отправляет результат
    encrypt_text_fernet, key_fernet = get_encrypt_text_fernet(message.text)
    encrypt_text_custom, key_custom = get_random_funcs((encrypt_text_fernet, key_fernet), size)
    bot.send_message(
        message.chat.id,
        f"🔐 *Зашифрованный текст:*\n`{encrypt_text_custom}`\n\n"
        f"🗝 *Ключ:*\n`{key_custom}`\n\n"
        "⚠️ *Не показывай эти данные никому!*",
        parse_mode="Markdown"
    )


@bot.message_handler(func=lambda m: m.text and m.text.lower().startswith('/decrypt'))
def decrypt(message: Message) -> None:
    # Запускает процесс расшифровки — запрашивает зашифрованный текст
    bot.send_message(message.chat.id, '🔐 Введи зашифрованное сообщение:')
    bot.register_next_step_handler(message, decrypt_input_crypt)


def decrypt_input_crypt(message: Message) -> None:
    # Получает зашифрованный текст, затем запрашивает ключ для расшифровки
    decrypt_text = message.text.strip()
    bot.send_message(message.chat.id, '🔑 Теперь введи ключ:')
    bot.register_next_step_handler(message, decrypt_input_key, decrypt_text)


def decrypt_input_key(message: Message, decrypt_text: str) -> None:
    # Получает ключ, пытается расшифровать текст (использует кастомное расшифрование, если ключ нестандартный)
    key = message.text.strip()
    if key[-1] != '=':
        decrypt_text_custom, key_custom = get_stock_crypt((decrypt_text, key))
    else:
        decrypt_text_custom, key_custom = decrypt_text, key
    decrypt_text_stock = get_decrypt_text_fernet(decrypt_text_custom, key_custom)

    if decrypt_text_stock.startswith("❌"):
        bot.send_message(message.chat.id, decrypt_text_stock)  # Ошибка расшифровки
    else:
        bot.send_message(
            message.chat.id,
            f"✅ Исходное сообщение:\n\n`{decrypt_text_stock}`",
            parse_mode="Markdown"  # Отправка результата в моноширинном формате для удобного копирования
        )


def main():
    # Устанавливает команды бота и запускает его опрос Telegram API
    bot.set_my_commands(commands)
    bot.polling(none_stop=True)
