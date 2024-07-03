import telebot
import sqlite3

bot = telebot.TeleBot('7352742662:AAHy0KFOrjt356Tt1024MywDE25b97vkQAk')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('citizen.db')  # Исправлено на sqlite3.connect
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введи свое имя.')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    pass

bot.polling(non_stop=True)