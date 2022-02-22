from telegram import Update ###
from telegram.ext import Updater, CommandHandler, CallbackContext ###

# Тестируем вызов функции hello_command
def hello_command(update: Update, context: CallbackContext): ###
    update.message.reply_text(f'Hello {update.effective_user.first_name}!') ###

# Тестируем вызов функции hello_command



updater = Updater('5224472726:AAGUN3lpLqGm2XLbgv7AFacCb-QjWFj0ScU') ###

updater.dispatcher.add_handler(CommandHandler('hello', hello_command)) ###

updater.start_polling() ###
updater.idle() ###

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