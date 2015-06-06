#!/usr/bin/env python
''' This code is not done!, don't judge me !''' 
''' Sound: https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview '''


import os, random
from time import sleep
from time import gmtime, strftime
import RPi.GPIO as GPIO

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

get_lock('sound')

current_milli_time = lambda: int(round(time.time() * 1000))

# Constants 
pathSoundEffects = '/sounds/'

#settings   
button_bounce = 500 

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
            os.system('mpg123 -q '+ os.getcwd() +  pathSoundEffects + self.fileName + ' &')
            
    def Check( self ) :
        if (GPIO.input( self.pinName ) == True):
            self.Play() 


randomButtonBounce = 0 
def PlayRandom() :
    global randomButtonBounce
    if randomButtonBounce + button_bounce < current_milli_time() :
        randomButtonBounce = current_milli_time()
        os.system('mpg123 -q '+ os.getcwd() +  pathSoundEffects + random.choice(os.listdir( os.getcwd() + pathSoundEffects )) + ' &') 

# Set up the Sound effects to GPIO pins 
# tell the GPIO module that we want to use 
# the chip's pin numbering scheme
GPIO.setmode(GPIO.BCM)

# special pin that is triggered by a bunch of buttons 
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

SoundEffectList = []

SoundEffectList.append(SoundEffect(4, "workit_loud.mp3" ))
SoundEffectList.append(SoundEffect(17, "makeit_loud.mp3" ))
SoundEffectList.append(SoundEffect(18, "doit_loud.mp3" ))
SoundEffectList.append(SoundEffect(27, "makeit.mp3" ))
SoundEffectList.append(SoundEffect(22, "workit.mp3" ))
SoundEffectList.append(SoundEffect(23, "makesus_loud.mp3" ))
SoundEffectList.append(SoundEffect(24, "harder_loud.mp3" ))
SoundEffectList.append(SoundEffect(25, "better_loud.mp3" ))
SoundEffectList.append(SoundEffect(6, "strong_loud.mp3" ))
SoundEffectList.append(SoundEffect(13, "morethen.mp3" ))
SoundEffectList.append(SoundEffect(16, "never_loud.mp3" ))
SoundEffectList.append(SoundEffect(37, "ever.mp3" ))
SoundEffectList.append(SoundEffect(12, "workit_loud.mp3" ))
# after.mp3, faster3.mp3


# main loop 
print 'Starting...'

#play a sound on start up. 
PlayRandom()
    
count = 0 
while True:    
    for button in SoundEffectList:
        button.Check() 
        
    if (GPIO.input( 5 ) == True):
        # play something random
        PlayRandom() 
