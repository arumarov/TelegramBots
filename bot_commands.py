from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hi_command(update: Update, context: CallbackContext): # в момент когда пользователь пришлет "hello", будет выполнена эта команда
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!') 
    
def help_command(update: Update, context: CallbackContext): 
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum') 

def time_command(update: Update, context: CallbackContext): 
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext): 
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')