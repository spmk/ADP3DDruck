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

run = False

def measure():
    if run == True:
        #Erstelle eine neue csv-datei:
        date_time = datetime.now().strftime("%y-%m-%d_%H-%M")
        path = os.path.dirname(__file__)+"/Data/" + date_time
        f = open("Data/" + date_time + ".csv", "w+")
        f_csv_writer = csv.writer(f,delimiter=",")
        row_index = 0
        
        try:
            while run == True:
                outputvalue = random.random()
                print(outputvalue, "") # Hier "" kann eine Einheit eingefuegt werden

                #Erstelle Inhalt der naechsten Reihe:
                row_time = datetime.now().strftime("%H/%M/%S")
                row_content = [row_index, row_time, outputvalue]
                row_index +=1
                #Schreibe die naeste Reihe:
                f_csv_writer.writerow(row_content)
            
                if outputvalue>limit:
                        statusLEDs.lightLed("warping")
                        Relais.statusDrucker("warping")
                        telegrambot.sendMessage()
                        time.sleep(20)
                        Relais.statusDrucker("no_warping")
                else: 
                        statusLEDs.lightLed("no_warping")
        finally:
            f.close() # Schliesse Daten.txt
            GPIO.cleanup()