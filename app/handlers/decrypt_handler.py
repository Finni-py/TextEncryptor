from telebot.types import Message

from app.bot_instance import bot
from app.utils.fernet_cryption import get_decrypt_text_fernet
from app.utils.custom_decryption import get_stock_crypt
from app.messages.message_text import GIVE_KEY, DEFAULT_MESSAGE


def decrypt_input_crypt(message: Message) -> None:
    # Получает зашифрованный текст, затем запрашивает ключ для расшифровки
    decrypt_text = message.text.strip()
    bot.send_message(message.chat.id, GIVE_KEY)
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
            DEFAULT_MESSAGE.format(decrypt_text_stock),
            parse_mode="Markdown"  # Отправка результата в моноширинном формате для удобного копирования
        )
