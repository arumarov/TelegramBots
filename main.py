from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5256574035:AAG5EheEO5-AZxRMGGLksWMYm5gbXfjV9oU')

updater.dispatcher.add_handler(CommandHandler('hello', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()