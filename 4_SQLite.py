import os
import telebot  # Импортируем библиотеку для работы с Telegram Bot API
import sqlite3  # Импортируем библиотеку для работы с SQLite
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена из переменной окружения
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Подключаемся к базе данных SQLite (если файл базы данных не существует, он будет создан)
    conn = sqlite3.connect('citizen.db')  # sqlite3.connect используется для подключения к базе данных
    cur = conn.cursor()  # Создаем курсор для выполнения SQL-запросов

    # Создаем таблицу users, если она еще не существует
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    pass TEXT
                )''')
    conn.commit()  # Подтверждаем изменения в базе данных
    cur.close()  # Закрываем курсор
    conn.close()  # Закрываем соединение с базой данных

    # Отправляем приветственное сообщение пользователю
    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введи свое имя.')
    # Регистрируем следующий шаг для обработки имени пользователя
    bot.register_next_step_handler(message, user_name)

# Функция для обработки имени пользователя
def user_name(message):
    pass  # Заглушка, здесь будет логика для обработки имени пользователя

# Запускаем бот в режиме непрерывного опроса
bot.polling(non_stop=True)
