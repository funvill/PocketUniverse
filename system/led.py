#!/usr/bin/env python
''' This code is not done!, don't judge me !''' 
''' Sound: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview '''


import os, random
from time import sleep
from time import gmtime, strftime
from bibliopixel.led import *
from bibliopixel.drivers.serial_driver import *
import bibliopixel.colors as colors


import socket
import sys
import time

def get_lock(process_name):
    global lock_socket   # Without this our lock gets garbage collected
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_socket.bind('\0' + process_name)
        print 'I got the lock'
    except socket.error:
        print 'lock exists'
        sys.exit()

get_lock('led')


# Constants 
countPixelStrip = 32*5 
ledCount = countPixelStrip * 8

#settings   
setting_speed = 10

driverA = 0 
driverB = 0 
led = 0 

def RestartLEDs( ):
    # set up the LEDs 
    print 'Restarting LEDs... ' 
    global driverA, driverB, led 
    driverA = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 2)
    driverB = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 1)
    led = LEDStrip([driverA, driverB])
    led.setMasterBrightness( 255/8 ) 

RestartLEDs( ); 

# main loop 
print 'Starting...'
count = 0 
while True:
    # Update the LEDs
    try :
        count += setting_speed 
        for pixel in range( ledCount ):
            led.set(pixel , colors.hue2rgb( (pixel + count) % 256 ) )
        led.update()
        
    except:
        RestartLEDs( );
