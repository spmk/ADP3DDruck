import time
import RPi.GPIO as GPIO
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BCM)
# Pin 22 (GPIO 25) als Ausgang festlegen
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)

while True:
    
    x = GPIO.input(5)
    print('Pin 5: ', x)
    y = GPIO.input(6)
    print('Pin 6: ', y)
    # eine Sekunden warten
    time.sleep(0.5)
