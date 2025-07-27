from cryptography.fernet import Fernet, InvalidToken


class FernetEncryptor:
    def __init__(self, key: str = None):
        if key:
            if isinstance(key, str):
                self.key = key.encode()
            else:
                self.key = key
        else:
            self.key = Fernet.generate_key()

    def encrypt_text_with_fernet(self, text: str) -> tuple[str, str]:
        # Шифрует текст и возвращает (ключ, зашифрованное сообщение)
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(text.encode())
        return self.key.decode(), encrypted_message.decode()

    def decrypt_text_with_fernet(self, encrypted_text: str) -> str:
        # Расшифровывает зашифрованный текст переданным ключом
        fernet = Fernet(self.key)
        decrypted_message = fernet.decrypt(encrypted_text.encode())
        return decrypted_message.decode()


def get_encrypt_text(text: str) -> tuple[str, str]:
    # Вызывает encrypt_text_with_fernet
    fernet_obj = FernetEncryptor()
    key, encrypted = fernet_obj.encrypt_text_with_fernet(text)
    return key, encrypted


def get_decrypt_text(encrypted_text: str, key: str) -> str:
    # Вызывает decrypt_text_with_fernet
    fernet_obj = FernetEncryptor(key=key)
    try:
        decrypted = fernet_obj.decrypt_text_with_fernet(encrypted_text)
    except InvalidToken:
        decrypted = "❌ Невозможно расшифровать: неверный ключ или повреждённое сообщение."
    return decrypted
