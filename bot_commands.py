from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hi_command(update: Update, context: CallbackContext): # в момент когда пользователь пришлет "hello", будет выполнена эта команда
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!') 
    
def help_command(update: Update, context: CallbackContext): 
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum') 

