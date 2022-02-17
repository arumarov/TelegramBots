from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5256574035:AAG5EheEO5-AZxRMGGLksWMYm5gbXfjV9oU')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
print('server start')
updater.start_polling()
updater.idle()