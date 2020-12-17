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
#Code wird nur ausgefuhrt, wenn execute direkt ausgefuehrt wird
def measure(): 
    if run == True:
        GPIO.setmode(GPIO.BCM)
        hx711 = HX711(dout_pin=5,pd_sck_pin=6,
                        gain_channel_A=64,select_channel='A')

        #hx711.reset()   #Before we start, reset the HX711 (not obligate)
        #hx711.zero()    #Offset eliminieren

        #Scale Ratio setzen
        scaleRatio = -1 #Spannungswert fuer Warping initial
        limit = 10000 #Wert, ab dem Warping erkannt wird
        averageOfXValues = 10 #Anzahl an Ausgelesenen Werten, die zur Auswertung gemittelt werden
        hx711.set_scale_ratio(scaleRatio)

        #Erstelle eine neue csv-datei:
        date_time = datetime.now().strftime("%y-%m-%d_%H-%M")
        path = os.path.dirname(__file__)+"/Data/" + date_time
        f = open("Data/" + date_time + ".csv", "w+")
        f_csv_writer = csv.writer(f,delimiter=",")
        row_index = 0

        #print("Values are saved to: " + date_time + ".csv")

        #Gewichte ausgeben, LEDs Relaise ansteuern
        print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
        print('Current value measured is: ')

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

        except (KeyboardInterrupt, SystemExit): #Programm kann mit Ctrl + C angehalten werden
            print("Pfiat di Gott! :D")

        finally:
            f.close() # Schliesse Daten.txt
            GPIO.cleanup()