from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telepot
from telepot.loop import MessageLoop
import execute

def hello(update: Update, context: CallbackContext) -> None:
    bot.sendMessage("473099318", "Everything is fine :)")
def start(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Ich mach noch nix")
    execute.run = True
    execute.measure()
def stop(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Ich mach noch nix")
    execute.run = False




bot = telepot.Bot('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY') #Token
updater = Updater('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY')


updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()