import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led1 = 3
led2 = 5
led3 = 7
led4 = 37
led5 = 35
led6 = 33
led7 = 31
led8 = 29
led9 = 11

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
    GPIO.cleanup()  
#    time.sleep(5000)
except KeyboardInterrupt:
 GPIO.cleanup()
 sys.exit(1)

