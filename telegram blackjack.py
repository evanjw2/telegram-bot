import os
import telebot

BOT_TOKEN = os.environ.get('7621604261:AAG4z2RzO6kowotr8ZpoJ-SGvzsxGoncPM4')

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


