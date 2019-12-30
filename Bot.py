#!/usr/bin/python3.5
import telebot
import bot_config

bot = telebot.TeleBot(bot_config.token)

def message_generait(text):
    if text == 'привет':
        return 'Привет, мой создатель'
    if text == 'пока':
        return 'Прощай, создатель'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
        bot.send_message(message.chat.id, message_generait(message.text.lower()))


bot.polling()