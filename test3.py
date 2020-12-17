#!/usr/bin/python3
from hx711 import HX711
import RPi.GPIO as GPIO
import time
from datetime import datetime
import csv
import os
import statusLEDs
import Relais
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telepot
from telepot.loop import MessageLoop
from multiprocessing import Process, Queue

# Telegram Bot
chat_id = "473099318"
Telegram_Token = '1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY'
bot = telepot.Bot(Telegram_Token)
updater = Updater(Telegram_Token)
status_Bot = 0
z=0
command = 0


# Telegram Bot Befehle definieren
def hello(update: Update, context: CallbackContext) -> None:
    bot.sendMessage(chat_id, "Everything is fine :)")

def start(update: Update, context: CallbackContext):
    bot.sendMessage(chat_id, "Queue true")
    command = 1
    bot.sendMessage(chat_id, command)
    
def stop(update: Update, context: CallbackContext):
    bot.sendMessage(chat_id, "Queue False")
    command = 'hallo'
    bot.sendMessage(chat_id, "Queue False")
    
# Telegram Poll-Loop

def a(queue):
    
    dp = updater.dispatcher # NICHT LÖSCHEN!
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    
    updater.start_polling()
    updater.idle()
    if command == 1:
        queue.put(True)
    else:
        queue.put(False)
    z=z+1
    print(z)
    

#Messschleife

def b(queue):
    
    GPIO.setmode(GPIO.BCM)
    hx711 = HX711(dout_pin=5,pd_sck_pin=6,
                    gain_channel_A=64,select_channel='A')
    
    # Erstelle eine neue csv-datei:
    date_time = datetime.now().strftime("%y-%m-%d_%H-%M")
    path = os.path.dirname(__file__)+"/Data/" + date_time
    f = open("Data/" + date_time + ".csv", "w+")
    f_csv_writer = csv.writer(f,delimiter=",")
    row_index = 0
    
    # Scale Ratio setzen
    scaleRatio = -1 # Spannungswert fuer Warping initial
    limit = 10000 # Wert, ab dem Warping erkannt wird
    averageOfXValues = 10 #Anzahl an Ausgelesenen Werten, die zur Auswertung gemittelt werden
    hx711.set_scale_ratio(scaleRatio)
    print("limit zugewiesen")
    
    while True:
        status = queue.get()
        outputvalue = random.random()
        print(outputvalue, "") # Hier "" kann eine Einheit eingefuegt werden

        # Erstelle Inhalt der naechsten Reihe:
        row_time = datetime.now().strftime("%H/%M/%S")
        row_content = [row_index, row_time, outputvalue]
        row_index +=1
        # Schreibe die naeste Reihe:
        f_csv_writer.writerow(row_content)

        if outputvalue > limit:
            statusLEDs.lightLed("warping")
            Relais.statusDrucker("warping")
            telegrambot.sendMessage()
            time.sleep(20)
            Relais.statusDrucker("no_warping")
        else:
            statusLEDs.lightLed("no_warping")
            
        if status == 0:
            break
            

        f.close() # Schliesse Daten.txt
        GPIO.cleanup()
        print("GPIO Cleanup complete!")
        



q = Queue()
p1 = Process(target=a, args=(q,))
p2 = Process(target=b, args=(q,))
p1.start()
p2.start()
p1.join()
p2.join()