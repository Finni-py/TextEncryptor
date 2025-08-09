from app.logger import logger

def decrypt_func_1(arg: tuple[str, str]) -> tuple[str, str]:
    # Обратная операция к перевороту строки: снова переворачивает сообщение
    message, key = arg
    return message[::-1], key[:-1]


def decrypt_func_2(arg: tuple[str, str]) -> tuple[str, str]:
    # Удаляет последние 3 символа из сообщения (обратная операция добавления 3 букв)
    message, key = arg
    return message[:-3], key[:-1]


def decrypt_func_3(arg: tuple[str, str]) -> tuple[str, str]:
    # Удаляет первые 3 символа из сообщения (обратная операция добавления 3 цифр в начало)
    message, key = arg
    return message[3:], key[:-1]


def decrypt_func_4(arg: tuple[str, str]) -> tuple[str, str]:
    # Удаляет первые 2 символа из сообщения (обратная операция добавления 2 случайных символов в начало)
    message, key = arg
    return message[2:], key[:-1]


def decrypt_func_5(arg: tuple[str, str]) -> tuple[str, str]:
    # Удаляет последние 3 символа из сообщения (обратная операция добавления 3 цифр в конец)
    message, key = arg
    return message[:-3], key[:-1]


def decrypt_func_6(arg: tuple[str, str]) -> tuple[str, str]:
    # Удаляет первый символ из сообщения (обратная операция добавления 1 буквы в начало)
    message, key = arg
    return message[1:], key[:-1]


def get_stock_crypt(arg: tuple[str, str]) -> tuple[str, str]:
    # Расшифровывает ключ и шифр к для расшифровки fernet
    message, key = arg
    while key[-1] != '=':
        last_char = key[-1]
        if last_char == 'z':
            message, key = decrypt_func_1((message, key))
        elif last_char == '7':
            message, key = decrypt_func_2((message, key))
        elif last_char == 'f':
            message, key = decrypt_func_3((message, key))
        elif last_char == 'k':
            message, key = decrypt_func_4((message, key))
        elif last_char == '5':
            message, key = decrypt_func_5((message, key))
        elif last_char == '9':
            message, key = decrypt_func_6((message, key))
        else:
            break
    logger.info('Расшифровано custom')
    return message, key
