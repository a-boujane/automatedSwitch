#!/usr/bin/python

import RPi.GPIO as GPIO
import time
#import datetime
import logging

#Selecting the GPIO for the sensor and the relay
sensor = 18
relay = 17
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN,GPIO.PUD_DOWN)
n=25
previous_state = False
current_state = False

#initializing the LOG file name
LOG_FILENAME='/home/pi/logs/AutomatedSwitch.log'

logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

try:
   while True:
      time.sleep(0.1)
      previous_state=current_state
      n=n+1
      if n==20:
         #logging.debug ('LOW - n==20, Cleaning up the relay')
        print "n==2, cleaning up relay" 
	GPIO.cleanup(relay)
      if n==100:
         n=30
      current_state=GPIO.input(sensor)
      if current_state != previous_state :
         new_state = "HIGH" if current_state else "LOW"
         print (new_state)
         while current_state:
            GPIO.setup(relay,GPIO.OUT)
            print "let's leave it on for 5 minutes"
            time.sleep(300)
            current_state=GPIO.input(sensor)
            n=0
except KeyboardInterrupt:
    GPIO.cleanup()
      

