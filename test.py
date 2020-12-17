from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import os

telegram_token = '1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY'

def start(bot, update):
    print("kp was ich hier mache")
    bot.send_message("473099318", "Jo Hoe Hoe")

u = Updater('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY',use_context = True)
u.start_polling()
u.idle