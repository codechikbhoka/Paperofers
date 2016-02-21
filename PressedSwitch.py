#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.IN)

decPins = [36,38,32,40]
inpPins = [24,22,18,26]

pressedPin  = -1

def readAllForData () : 
 for i in range(0,4) :
  if(GPIO.input(inpPins[i]) == GPIO.HIGH ):
   return i
 return -1			

def checkSwitch() :
        while True :
                for i in range(0,4) :
                        for j in decPins:
                            GPIO.output(j,0)
                        GPIO.output(decPins[i],1)
                        time.sleep(0.05)
                        pinNum = readAllForData()
                        #if pinNum == lastRead:
                        #        count += 1
                        #print str(i) + " " +str(pinNum) 
                        if pinNum != -1 :
                                #count = 0
                             #   lastPinNum = pinNum
                                switchNum = calculateSwitchNumber(i,pinNum)	
                                pressSwitch(switchNum)
                        #lastRead = pinNum

def writeToFile(x):
    f = open("pin.txt", "w")
    f.write(x)
    f.close()

def calculateSwitchNumber(decPin,pinNum) :
	return 4*(decPin) + pinNum + 1		

def pressSwitch(switchNum) : 
	print str(switchNum)  + " pressed"
	writeToFile(str(switchNum))
	pressedPin = switchNum
	#time.sleep(0.05)



try:
 while True :
	checkSwitch()
	#time.sleep(sleepTime) 
except KeyboardInterrupt:
 GPIO.cleanup()



