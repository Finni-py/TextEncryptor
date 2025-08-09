# 🛡️ Telegram Encryption Bot

Простой **Telegram-бот** для шифрования и расшифровки сообщений, использующий библиотеку **Fernet** и кастомные методы.

## 🚀 Возможности

- 🔐 Шифрование текста с генерацией ключа
- 🔓 Расшифровка зашифрованного текста по ключу
- ⚙️ Несколько уровней сложности шифрования
- 🧩 Кастомные функции для дополнительной защиты
- 🧑‍💻 Удобный интерфейс с интерактивными кнопками
- 📎 Обработка ошибок и валидация ввода

---

## 🛠️ Стек технологий

![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)
![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-05122A?style=flat&logo=telegram)
![🛡️ Fernet](https://img.shields.io/badge/🛡️-Fernet-05122A?style=flat)
![python-dotenv](https://img.shields.io/badge/%F0%9F%8C%BF-python--dotenv-05122A?style=flat)

## 🗂️ Структура проекта

```
TextEncryptor/
└── app/
    ├── handlers/                 # Папка с обработчиками команд и сообщений
    │   ├── __init__.py           # Инициализация пакета handlers
    │   ├── decrypt_handler.py    # Обработчик для расшифровки текста
    │   ├── encrypt_handler.py    # Обработчик для шифрования текста
    │   └── start_handler.py      # Обработчик команды /start
    ├── messages/                 # Тексты сообщений, шаблоны для ответов бота
    │   ├── __init__.py           # Инициализация пакета messages
    │   └── message_text.py       # Хранение текстов сообщений для бота
    ├── utils/                    # Вспомогательные утилиты и алгоритмы
    │   ├── __init__.py           # Инициализация пакета utils
    │   ├── custom_decryption.py  # Функции для кастомной расшифровки
    │   ├── custom_encryption.py  # Функции для кастомного шифрования
    │   └── fernet_cryption.py    # Шифрование/расшифровка с использованием fernet
    ├── bot_instance.py           # Инициализация и настройка экземпляра Telegram-бота
    ├── config.py                 # Конфигурационные параметры проекта (токены, настройки)
    ├── telegram_bot.py           # Основной модуль бота, обработка обновлений и запуск
    ├── README.md
    ├── .env
    └── .gitignore

```

---

## 📦 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/telegram-encryption-bot.git
cd telegram-encryption-bot
```

### 2. Создание виртуального окружения (рекомендуется)

```bash
python -m venv venv
```

### 3. Активация виртуального окружения

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Запуск бота

```bash
python app/main.py
```

## 💬 Использование

1. Запустите бота в Telegram.
2. Используйте команды:

    - `/start` — запуск
    - `/encrypt` — шифрование сообщения
    - `/decrypt` — расшифровка
    - `/help` — помощь
    - `/github` — ссылка на исходный код

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Свободно используй, дорабатывай и распространяй с указанием авторства.

## 👤 Автор

- GitHub: [@finniy](https://github.com/finniy)
- Telegram: [@fjnnjk](https://t.me/fjnnjk)

💌 Не забудьте поставить звезду ⭐ на GitHub, если вам понравился бот! 😉