#!/usr/bin/env python
 
import os
from time import sleep
from time import gmtime, strftime
 
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

count = 0 
 
while True:
    if (GPIO.input(17) == False):
        count += 1 
        print "%d) pin=17" % count 
		
    sleep(0.1);
