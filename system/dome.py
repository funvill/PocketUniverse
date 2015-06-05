#!/usr/bin/env python
''' This code is not done!, don't judge me !''' 
''' Sound: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview '''


import os
from time import sleep
from time import gmtime, strftime
from bibliopixel.led import *
from bibliopixel.drivers.serial_driver import *
import bibliopixel.colors as colors
import Adafruit_BBIO.GPIO as GPIO

# Constants 
countPixelStrip = 32*5 
ledCount = countPixelStrip * 8

#settings   
setting_speed = 10
 
# set up the LEDs 
driverA = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 2)
driverB = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 1)
led = LEDStrip([driverA, driverB])
led.setMasterBrightness( 255/8 ) 

class SoundEffect(object):
    def __init__(self, pinName=None, fileName=None) :
         self.pinName = pinName
         self.fileName = fileName
         
         GPIO.setup( self.pinName , GPIO.IN)        
         GPIO.add_event_detect( self.pinName, GPIO.RISING)
         
         # debug 
         print self.pinName + ' ' + self.fileName  


# Set up the Sound effects to GPIO pins 

SoundEffectList = []
SoundEffectList.append(SoundEffect("P8_3", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_5", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_7", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_9", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_11", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_13", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_15", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_17", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_19", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_21", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_23", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_25", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_27", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_29", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_31", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_33", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_35", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_37", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_39", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_41", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_43", "one.mp3" ))
SoundEffectList.append(SoundEffect("P8_45", "one.mp3" ))
    

# main loop 
print 'Starting...'
count = 0 
while True:
    
    # Update the LEDs 
    count += setting_speed 
    for pixel in range( ledCount ):
        led.set(pixel , colors.hue2rgb( (pixel + count) % 256 ) )
    led.update()
     
    # check the GPIO pins 
    for button in SoundEffectList:
        if GPIO.event_detected( button.pinName ):
            print button.pinName + " event detected "
            # Play the sound effect 
            os.system('mpg123 -q '+ button.fileName + ' &')  
     