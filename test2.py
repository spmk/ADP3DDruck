from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telepot
from telepot.loop import MessageLoop
import execute

chat_id = "473099318"
Telegram_Token = '1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY'

def hello(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Everything is fine :)")
    
def start(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Ich mach noch nix")
    execute.run = True
    

def stop(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Ich mach noch nix")
    execute.run = False



x=1
x=x+1
print(x)

p = Process(target=execute.measure, args=())
# you have to set daemon true to not have to wait for the process to join
p.daemon = True
p.start()
print("doing stuff in the background")

bot = telepot.Bot(Telegram_Token)
updater = Updater(Telegram_Token)

dp = updater.dispatcher #Dieser ficker sorgt dafür, dass neue Befehle gefunden werden
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("stop", stop))

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()