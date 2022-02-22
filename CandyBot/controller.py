from telegram import Update ###
from telegram.ext import Updater, CommandHandler ###
from bot_commands import *


updater.dispatcher.add_handler(CommandHandler('hi', hello_command))

updater = Updater('5224472726:AAGUN3lpLqGm2XLbgv7AFacCb-QjWFj0ScU') ###

print('server start')
updater.start_polling()
updater.idle()




def click_button():
    print('Hi')