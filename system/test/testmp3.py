#!/usr/bin/env python
''' From https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview '''
import os 
from time import sleep 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 

while True:
    if (GPIO.input(17) == True):
        os.system('mpg123 -q workit.mp3 &')
    if (GPIO.input(27) == True):
        os.system('mpg123 -q harder.mp3 &')

    sleep(0.1);
