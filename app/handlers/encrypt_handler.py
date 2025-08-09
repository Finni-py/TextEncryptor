from telebot.types import Message

from app.bot_instance import bot
from app.utils.custom_encryption import get_random_funcs
from app.utils.fernet_cryption import get_encrypt_text_fernet
from app.messages.message_text import ENCRYPT_SECOND_TEXT
from app.messages.message_text import NO_LEVEL


def work_with_input_size(message: Message) -> None:
    # Получает уровень сложности от пользователя, проверяет его и просит ввести текст для шифрования
    try:
        size = int(message.text)
        if 1 <= size <= 3:
            bot.send_message(message.chat.id, ENCRYPT_SECOND_TEXT)
            bot.register_next_step_handler(message, encrypt_input_info, size)
        else:
            raise ValueError
    except ValueError:
        bot.send_message(message.chat.id, NO_LEVEL)
        bot.register_next_step_handler(message, work_with_input_size)


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
