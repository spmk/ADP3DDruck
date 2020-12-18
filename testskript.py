import time
import RPi.GPIO as GPIO
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)


while True:
    
    x = GPIO.input(5)
    print('Pin 5: ' + x)
    y = GPIO.input(6)
    print('Pin 6: ' + y)
    # eine Sekunden warten
    time.sleep(0.5)

# Ausgänge wieder freigeben
GPIO.cleanup()