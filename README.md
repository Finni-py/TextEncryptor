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

# Установка

### Создание виртуального окружения (рекомендуется)
```bash
python -m venv venv
```
### Windows:

```bash
venv\Scripts\activate
```
### macOS/Linux:

```bash
source venv/bin/activate
```
### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Запуск бота
```bash
python app/main.py
```

## Команды бота

- /start — запуск и приветствие
- /encrypt — начать процесс шифрования
- /decrypt — начать процесс расшифровки
- /help — список команд
- /github — ссылка на репозиторий проекта

### Лицензия
Этот проект лицензирован под MIT License.