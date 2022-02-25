from telegram import Update ###
from telegram.ext import Updater, CommandHandler, CallbackContext ###
import random ###

# Тестируем вызов функции hello_command (приветствие пользователя)
# def hello_command(update: Update, context: CallbackContext): ###
#     update.message.reply_text(f'Hello {update.effective_user.first_name}!') ###

# Тестируем вызов функции start_candy (стартовое сообщение)
# def start_candy():
#     global sum
#     global g
#     g = 2021
#     sum = (f'Количество конфет на столе: {g}.')
#     sum1 = (f'\nПервый ход определяется жеребьевкой. \nЗа один ход можно забрать не более 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход. \nПроведем жеребьевку? Введите 1 или 2')
#     return sum + sum1

# Тестируем вызов функции choice_move (СДЕЛАНА В ОФЛАЙНЕ, АДАПТИРОВАТЬ ПОД ТЕЛЕГРАМ)

# def choice_move():
#     choice = random.randint(1, 2)
#     message = 'Жеребьевка! Выберите число: 1 или 2'
#     print(message)
#     mes1 = int(input())
#     if mes1 != 1 and mes1 != 2: res = choice_move()
#     elif mes1 == choice: res = 'Вы ходите первым'
#     elif mes1 != choice: res = 'Компьютер ходит первым'
#     return res
# print(choice_move())
    # update.message.reply_text(f'Жеребьевка {update.effective_user.first_name}!')

# Тестируем вызов функции game_candy

def game_candy():
    





# updater = Updater('5224472726:AAGUN3lpLqGm2XLbgv7AFacCb-QjWFj0ScU') ###

# updater.dispatcher.add_handler(CommandHandler('hello', hello_command)) ###

# updater.start_polling() ###
# updater.idle() ###

# import datetime
# from spy import *

# def help_command(update: Update, context: CallbackContext): 
#     log(update, context)
#     update.message.reply_text(f'/hi\n/time\n/help\n/sum') #возвращает помощь

# def time_command(update: Update, context: CallbackContext): 
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')

# def sum_command(update: Update, context: CallbackContext): 
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split(' ') # /sum 123 5343532
#     x = int(items[1])
#     y = int(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}') #возвращает помощь