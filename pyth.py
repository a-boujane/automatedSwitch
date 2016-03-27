##This is going to be a multithreaded version of the switch relay to run a
##counter that is going to be reset everytime motion==1. 
#Only at the end of the counter we are going to turn off the light
#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from datetime import datetime as dt
import Queue
import threading
global sensor
sensor = 18
global relay
relay= 17



def initialSetup ():
        GPIO.cleanup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor,GPIO.IN,GPIO.PUD_DOWN)

def ifMotionThenResetTimer(Q):
        tt=int(time.time())
        while True:             
                motion = GPIO.input(sensor)
                time.sleep(0.1)
                if motion and Q.empty():
                        tt=int(time.time())
                        print now()" -- motion detected!"
                        Q.put(tt)
                        time.sleep(2)

def ifTimerThenTurnOnOrOff(Q):
        alreadyOn=False
        
        tt=int(time.time())
        while True:
                time.sleep(0.1)
                if not Q.empty():
                        tt=Q.get()
                t=int(time.time())
                delta = t-tt
                #print delta
                if delta<300 and not alreadyOn:
                        print "if t-t0<10 and not alreadyOn:"
                        turnOn()
                        alreadyOn=True
                elif delta>=300 and alreadyOn:
                        print "elif t-t0>=10 and not alreadyOn:"
                        turnOff()
                        alreadyOn=False
                time.sleep(0.1)
                
               
def turnOn():
        print "entered turnOn()"
        print "going HIGH now"
        GPIO.setup(relay,GPIO.OUT)

def turnOff():
        print "Entered turnOff()"
        print "Going LOW now"
        GPIO.cleanup(relay)

def now():
	return dt.now().strftime("%A %B, %d %Y, %H:%M:%S")

initialSetup()
Q=Queue.Queue()

Thread1=threading.Thread(target=ifMotionThenResetTimer, args=(Q,))
Thread2=threading.Thread(target=ifTimerThenTurnOnOrOff, args=(Q,))
print "Starting Thread1, then Thread2"
Thread1.start()
Thread2.start()

        
