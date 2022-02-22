from telegram import Update ###
from telegram.ext import Updater, CommandHandler, CallbackContext ###



updater = Updater('5224472726:AAGUN3lpLqGm2XLbgv7AFacCb-QjWFj0ScU') ###


updater.start_polling()
updater.idle()