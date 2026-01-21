import RPi.GPIO as GPIO
import time

LED_PIN = 10  # GPIO10 = Pin 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # เปิดไฟ
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)   # ปิดไฟ
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
