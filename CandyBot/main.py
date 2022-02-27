from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from bot_commands import *

updater = Updater('5224472726:AAGUN3lpLqGm2XLbgv7AFacCb-QjWFj0ScU')

updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('start', start_candy))
updater.dispatcher.add_handler(CommandHandler('choice', choice_move))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

print('server start')
updater.start_polling()
updater.idle()