##This is going to be a multithreaded version of the switch relay to run a
##counter that is going to be reset everytime motion==1. 
#Only at the end of the counter we are going to turn off the light
#!/usr/bin/python

import RPi.GPIO as GPIO
import time
sensor = 4
relay = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN,GPIO.PUD_DOWN)
n=25
previous_state = False
current_state = False
try:
   while True:
      time.sleep(0.1)
      previous_state=current_state
      n=n+1
      if n==20:
         print "LOW"
         GPIO.cleanup(relay)
      if n==100:
         n=30
      current_state=GPIO.input(sensor)
      if current_state != previous_state :
         new_state = "HIGH" if current_state else "LOW"
         print (new_state)
         while current_state:
            GPIO.setup(relay,GPIO.OUT)
            print ("let's leave it on for 120 seconds")
            time.sleep(120)
            current_state=GPIO.input(sensor)
            n=0
except KeyboardInterrupt:
    GPIO.cleanup()
      

