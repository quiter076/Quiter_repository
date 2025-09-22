import telebot
token = '8495971064:AAHFlqhm3ZZVcqCnOQLjMxXVK-N4B-4PtX0'
bot = telebot.Telebot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.sendmessage