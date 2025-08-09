# 🛡️ Telegram Encryption Bot

Простой **Telegram-бот** для шифрования и расшифровки сообщений, использующий библиотеку **Fernet** и кастомные методы.

---

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
![logger](https://img.shields.io/badge/%E2%9A%A0-logger-05122A?style=flat&logo=logging)
![python-dotenv](https://img.shields.io/badge/%F0%9F%8C%BF-python--dotenv-05122A?style=flat)

---

## 🗂️ Структура проекта

```
TextEncryptor/
└── app/
    ├── handlers/
    │   ├── __init__.py
    │   ├── decrypt_handler.py
    │   ├── encrypt_handler.py
    │   └── start_handler.py
    ├── messages/ 
    │   ├── __init__.py  
    │   └── message_text.py    
    ├── utils/               
    │   ├── __init__.py      
    │   ├── custom_decryption.py  
    │   ├── custom_encryption.py 
    │   └── fernet_cryption.py   
    ├── bot_instance.py      
    ├── config.py    
    ├── logger.py         
    ├── telegram_bot.py     
    ├── README.md
    ├── .env
    └── .gitignore

```

---

## 📦 Установка

### 1. Клонирование репозитория

```bash
git clone https://https://github.com/finniy/TextEncryptor.git
cd TextEncryptor
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

---

## 👤 Автор

- GitHub: [@finniy](https://github.com/finniy)
- Telegram: [@fjnnjk](https://t.me/fjnnjk)

💌 Не забудьте поставить звезду ⭐ на GitHub, если вам понравился бот! 😉