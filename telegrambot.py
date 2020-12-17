#!/usr/bin/python3
import telepot
import time
from telepot.loop import MessageLoop
import statusLEDs
import execute

#Hier sind alle Befehle definiert, die der Bot ausfuehren kann.
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	print('Got command: %s' % command)
	
	if command == '/status':
		bot.sendMessage(chat_id, "Everything is fine :)")
	elif command == '/warpingLED':
		bot.sendMessage(chat_id, "Red LED is turned on!")
		statusLEDs.lightLed("warping")
	elif command == '/no_warpingLED':
		bot.sendMessage(chat_id, "Green LED is turned off!")
		statusLEDs.lightLed("no_warping")
	elif command == '/help':
		bot.sendMessage(chat_id, "/start - Start the Warping Detective \n /stop - Stop the Warping Detective \n /status - Sends status if warping occured \n /warpingLED - Turns on RED LED \n /no_warpingLED - Turns on GREEN LED")
	elif command == '/start':
		bot.sendMessage(chat_id, "Ich mach noch nix")
		execute.run = True
		execute.measure()
	elif command == '/stop':
		bot.sendMessage(chat_id, "Ich mach noch nix")
		execute.run = False

#Bot Objekt wird erstellt und diesem werden die Befehle uebergeben
bot = telepot.Bot('1435246331:AAEuTzd96pMR8ACXl92za8CSFo_0gd1QCvY') #Token
MessageLoop(bot, handle).run_as_thread()
print(bot)

#Boot up Nachricht des Bots:
print("Hi! I am your personal warping assistant!") #Auf der Konsole
bot.sendMessage("473099318", "Hi I am your personal warping assistent!") #In Telegram
bot.sendMessage("473099318", "I will text you if warping occurs.") #In Telegram

#Diese Methode wird in execute.py aufgerufen, wenn Warping auftritt. 
def send_Message():
	bot.sendMessage("473099318", "Warping erkannt und Drucker abgeschaltet!")