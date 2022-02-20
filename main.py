import telebot
import random
from telebot import types

w = open('words.txt', 'r', encoding='UTF-8')
words = w.read().split('\n')
w.close()

bot = telebot.TeleBot('5212071316:AAFGsl3UO8zlFGW_4roTLrXZk1VBUL3GNeY')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Карточка")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Нажми: \nКарточка для получения следующей карточки',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему следующую карточку
    if message.text.strip() == 'Карточка' :
        answer = random.choice(words)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True, interval=0)
# bot.polling()