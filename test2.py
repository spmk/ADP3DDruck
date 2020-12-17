from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telepot


def hello(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Everything is fine :)")
    update.message.reply_text(f'Hello {update.effective_user.Joshua}')
    
updater = Updater('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()