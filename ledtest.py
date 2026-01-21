import RPi.GPIO as GPIO
import time

LED_PINS = [10, 25, 7]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PINS, GPIO.OUT)

try:
    while True:
        for pin in LED_PINS:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
