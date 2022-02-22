from telegram import Update ###
from telegram.ext import Updater, CommandHandler, CallbackContext ###

def hello_command(update: Update, context: CallbackContext): ###
    update.message.reply_text(f'Hello {update.effective_user.first_name}!') ###

def start_candy():
    res = (f'На столе лежит'  )