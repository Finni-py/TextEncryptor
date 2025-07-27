import random
import string


def encrypt_func_1(arg: tuple[str, str]) -> tuple[str, str]:
    # Функция переворачивает сообщение и добавляет 'z' к ключу
    message, key = arg
    return message[::-1], key + 'z'


def encrypt_func_2(arg: tuple[str, str]) -> tuple[str, str]:
    # Функция добавляет к сообщению 3 случайные латинские буквы и добавляет '7' к ключу
    message, key = arg
    return message + ''.join(random.choice(string.ascii_letters) for _ in range(3)), key + '7'


def encrypt_func_3(arg: tuple[str, str]) -> tuple[str, str]:
    # Функция добавляет в начало сообщения случайное число от 000 до 999 и добавляет 'f' к ключу
    message, key = arg
    return f'{random.randint(0, 999):03d}' + message, key + 'f'


def encrypt_func_4(arg: tuple[str, str]) -> tuple[str, str]:
    # Функция добавляет в начало сообщения 2 случайных символа из заданного набора и добавляет 'k' к ключу
    message, key = arg
    return ''.join(random.choice('d=-3402_9d93') for _ in range(2)) + message, key + 'k'


def encrypt_func_5(arg: tuple[str, str]) -> tuple[str, str]:
    # Функция добавляет к сообщению случайное число от 000 до 011 и добавляет '5' к ключу
    message, key = arg
    return message + f'{random.randint(0, 11):03d}', key + '5'


def encrypt_func_6(arg: tuple[str, str]) -> tuple[str, str]:
    # Функция добавляет в начало сообщения 1 случайную латинскую букву и добавляет '9' к ключу
    message, key = arg
    return ''.join(random.choice(string.ascii_letters) for _ in range(1)) + message, key + '9'


encryption_funcs = [
    encrypt_func_1,
    encrypt_func_2,
    encrypt_func_3,
    encrypt_func_4,
    encrypt_func_5,
    encrypt_func_6,
]


def get_random_funcs(arg_stock: tuple[str, str]) -> tuple[str, str]:
    # Применяет случайное количество (от 10 до 50) случайных функций из списка к аргументу
    arg = arg_stock
    random_num = random.randint(10, 50)
    for _ in range(random_num):
        random_func = random.choice(encryption_funcs)
        arg = random_func(arg)
    print('[+] Зашифровано custom')
    return arg
