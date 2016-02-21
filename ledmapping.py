import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led1 = 11
led2 = 29
led3 = 31
led4 = 33
led5 = 7
led6 = 5
led7 = 3
led8 = 37
led9 = 35

ledmap = [led1, led2, led3, led4, led5, led6, led7, led8, led9]

def setup():
 GPIO.cleanup()
   
 GPIO.setup(32, GPIO.OUT)
 GPIO.setup(36, GPIO.OUT)
 GPIO.setup(38, GPIO.OUT)
 GPIO.setup(40, GPIO.OUT)
   
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(led2, GPIO.OUT)
 GPIO.setup(led3, GPIO.OUT)
 GPIO.setup(led4, GPIO.OUT)
 GPIO.setup(led5, GPIO.OUT)
 GPIO.setup(led6, GPIO.OUT)
 GPIO.setup(led7, GPIO.OUT)
 GPIO.setup(led8, GPIO.OUT)
 GPIO.setup(led9, GPIO.OUT)

def turnOnLED(led_number):
 GPIO.output(led_number, 1)

def turnOffLED(led_number):
 GPIO.output(led_number, 0)

def turnOfAll():
 for i in ledmap :
     turnOffLED(i)

try:
    setup()
    for i in ledmap : 
        turnOfAll()
        turnOnLED(i)
        time.sleep(1)

#    time.sleep(5000)
except KeyboardInterrupt:
 GPIO.cleanup()
 sys.exit(1)

