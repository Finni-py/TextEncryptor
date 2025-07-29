# Telegram Encryption Bot

Простой Telegram-бот для шифрования и расшифровки сообщений с использованием библиотеки Fernet и кастомных методов.

## Возможности

- Шифрование текста с генерацией ключа
- Расшифровка зашифрованного текста по ключу
- Несколько уровней сложности шифрования
- Кастомные функции для дополнительной защиты
- Удобный интерактивный интерфейс с кнопками

## Используемые технологии

- Python 3.8+
- [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)
- [cryptography (Fernet)](https://cryptography.io/en/latest/)
- Стандартная библиотека Python

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/finniy/TextEncryptor.git
   cd TextEncryptor


2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте в него ваш API ключ Telegram:

   ```
   API_KEY=ваш_токен_бота
   ```

4. Запустите бота:

   ```bash
   python bot.py
   ```

---

## Команды бота

- /start — запуск и приветствие
- /encrypt — начать процесс шифрования
- /decrypt — начать процесс расшифровки
- /help — список команд
- /github — ссылка на репозиторий проекта

### Лицензия
Этот проект лицензирован под MIT License.