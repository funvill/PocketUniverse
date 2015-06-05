#!/usr/bin/env python
''' This code is not done!, don't judge me !''' 
''' Sound: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview '''


import os
from time import sleep
from time import gmtime, strftime
from bibliopixel.led import *
from bibliopixel.drivers.serial_driver import *
import bibliopixel.colors as colors
import RPi.GPIO as GPIO

current_milli_time = lambda: int(round(time.time() * 1000))

# Constants 
countPixelStrip = 32*5 
ledCount = countPixelStrip * 8

#settings   
setting_speed = 10
button_bounce = 500 
 
# set up the LEDs 
driverA = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 2)
driverB = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 1)
led = LEDStrip([driverA, driverB])
led.setMasterBrightness( 255/8 ) 

class SoundEffect(object):
    def __init__(self, pinName=None, fileName=None) :
         self.pinName = pinName
         self.fileName = fileName
         self.lastPlay = 0          
         GPIO.setup(self.pinName, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
           
    def Play(self) : 
        if self.lastPlay + button_bounce < current_milli_time() :
            self.lastPlay = current_milli_time()            
            print 'Pin=%d, Play MP3 %s' %( self.pinName, self.fileName )
            os.system('mpg123 -q '+ self.fileName + ' &')
            
    def Check( self ) :
        if (GPIO.input( self.pinName ) == True):
            self.Play() 


# Set up the Sound effects to GPIO pins 
# tell the GPIO module that we want to use 
# the chip's pin numbering scheme
GPIO.setmode(GPIO.BCM)


SoundEffectList = []
SoundEffectList.append(SoundEffect(4, "harder.mp3" ))
SoundEffectList.append(SoundEffect(17, "doit.mp3" ))
SoundEffectList.append(SoundEffect(18, "better.mp3" ))
SoundEffectList.append(SoundEffect(27, "makeit.mp3" ))
SoundEffectList.append(SoundEffect(22, "workit.mp3" ))
SoundEffectList.append(SoundEffect(23, "harder.mp3" ))
SoundEffectList.append(SoundEffect(24, "harder.mp3" ))
SoundEffectList.append(SoundEffect(25, "harder.mp3" ))
SoundEffectList.append(SoundEffect(5, "harder.mp3" ))
SoundEffectList.append(SoundEffect(6, "harder.mp3" ))
# SoundEffectList.append(SoundEffect(12, "harder.mp3" ))
SoundEffectList.append(SoundEffect(13, "harder.mp3" ))
SoundEffectList.append(SoundEffect(16, "harder.mp3" ))
SoundEffectList.append(SoundEffect(37, "harder.mp3" ))



# main loop 
print 'Starting...'
count = 0 
while True:
 
    for button in SoundEffectList:
        button.Check() 

    # Update the LEDs 
    count += setting_speed 
    for pixel in range( ledCount ):
        led.set(pixel , colors.hue2rgb( (pixel + count) % 256 ) )
    led.update()
                 
     