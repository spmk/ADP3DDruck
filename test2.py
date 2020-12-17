from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    bot.sendMessage('473099318', "i work!")
    
    
bot.sendMessage('473099318', "Everything is fine :)")
updater = Updater('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()