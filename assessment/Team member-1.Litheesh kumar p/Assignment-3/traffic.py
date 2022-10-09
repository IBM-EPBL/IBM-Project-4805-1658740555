import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
while True:
    GPIO.output(8,GPIO.HIGH)
    sleep(1)
    GPIO.output(10,GPIO.LOW)
    sleep(1)
    GPIO.output(11,GPIO.LOW)
    sleep(1)
    GPIO.output(8,GPIO.LOW)
    sleep(1)
    GPIO.output(10,GPIO.HIGH)
    sleep(1)
    GPIO.output(11,GPIO.LOW)
    sleep(1)
    GPIO.output(8,GPIO.LOW)
    sleep(1)
    GPIO.output(10,GPIO.LOW)
    sleep(1)
    GPIO.output(11,GPIO.HIGH)
    sleep(1)
    
    
