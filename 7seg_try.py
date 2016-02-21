# code modified, tweaked and tailored from code by bertwert 
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
 
# GPIO ports for the 7seg pins
segments =  (8,5,7,11,10,15,19)
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
# GPIO ports for the digit pins 
digits = (12,18)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


GPIO.output(12, 0)
GPIO.output(18, 1)
 
num = {' ':(0,0,0,0,0,0,0),
    0:(0,0,0,0,0,0,1),
    1:(1,0,0,1,1,1,1),
    2:(0,0,1,0,0,1,0),
    3:(0,0,0,0,1,1,0),
    4:(1,0,0,1,1,0,0),
    5:(0,1,0,0,1,0,0),
    6:(0,1,0,0,0,0,0),
    7:(0,0,0,1,1,1,1),
    8:(0,0,0,0,0,0,0),
    9:(0,0,0,0,1,0,0)}
 
numDebug = {' ':(1,1,1,1,1,1,1),
    '0':(1,1,1,1,1,1,0),
    '1':(1,1,1,1,1,0,1),
    '2':(1,1,1,1,0,1,1),
    '3':(1,1,1,0,1,1,1),
    '4':(1,1,0,1,1,1,1),
    '5':(1,0,1,1,1,1,1),
    '6':(0,1,1,1,1,1,1)
}


def printNum(number):
 arrayA = num[number]
 for i in range(0,7):
  GPIO.output(segments[i], arrayA[i])


def printAtDigit1(num):
 GPIO.output(12, 0)
 GPIO.output(18, 1)
 printNum(num)



def printAtDigit2(num):
 GPIO.output(12, 1)
 GPIO.output(18, 0)
 printNum(num)



def outputNumber(num):
 while 1:
  printAtDigit1(num%10)
  time.sleep(0.005)
  printAtDigit2(num/10)
  time.sleep(0.005)

#for i in range(0, 10):
# printAtDigit1(i)
# time.sleep(2)

try:
 outputNumber(69)
finally:
 GPIO.cleanup()




GPIO.cleanup()
