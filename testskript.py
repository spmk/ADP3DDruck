import time
import RPi.GPIO as GPIO
# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)
# Pin 22 (GPIO 25) als Ausgang festlegen
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
# Ausgang 3 mal ein-/ausschalten

while True:
    
    x = GPIO.input(5) == GPIO.HIGH:
    print('Pin 5: ' + x)
    y = GPIO.input(6) == GPIO.HIGH:
    print('Pin 6: ' + y)
    # eine Sekunden warten
    time.sleep(0.5)

# Ausgänge wieder freigeben
GPIO.cleanup()