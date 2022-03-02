from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
import random


def hello_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext): 
    update.message.reply_text(f'/hello\n/start\n/help\n/choice')

def start_candy(update: Update, context: CallbackContext):
    global sum
    global g
    g = 100
    sum = (f'Количество конфет на столе: {g}.')
    sum1 = (f'\nПервый ход определяется жеребьевкой. \nЗа один ход можно забрать не более 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход. \nПроведем жеребьевку?')
    update.message.reply_text(sum + sum1)
    choice_move()


def choice_move(update: Update, context: CallbackContext):
    choice = random.randint(1, 2)
    update.message.reply_text('Жеребьевка! Введите число: 1 или 2: ')
    mes = update.message.from_user
    update.message.reply_text(mes)
    mes1 = int(mes)
    if mes1 != 1 and mes1 != 2: choice_move
    elif mes1 == choice: res = 'Вы ходите первым'
    elif mes1 != choice: res = 'Компьютер ходит первым'
    update.message.reply_text(res)

