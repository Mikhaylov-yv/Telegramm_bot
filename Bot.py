#!/usr/bin/python3.5
import telebot
import bot_config

print('Бобр')
bot = telebot.TeleBot(bot_config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()