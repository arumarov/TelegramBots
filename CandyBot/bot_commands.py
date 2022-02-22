from telegram import Update ###
from telegram.ext import Updater, CommandHandler, CallbackContext ###

def hello_command(update: Update, context: CallbackContext): ###
    update.message.reply_text(f'Hello {update.effective_user.first_name}!') ###



updater = Updater('5224472726:AAGUN3lpLqGm2XLbgv7AFacCb-QjWFj0ScU') ###





updater.start_polling()
updater.idle()