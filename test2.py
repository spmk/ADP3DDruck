from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telepot
from telepot.loop import MessageLoop


def hello(update: Update, context: CallbackContext) -> None:
    bot.sendMessage("473099318", "Everything is fine :)")
    update.message.reply_text(f'Hello {update.effective_user.Joshua}')
bot = telepot.Bot('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY')    
updater = Updater('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()