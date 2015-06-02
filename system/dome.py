#!/usr/bin/env python
''' This code is not done!, don't judge me !''' 
import os
import RPi.GPIO as GPIO
from time import sleep
from time import gmtime, strftime
from bibliopixel.drivers.serial_driver import *
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)

count = 0 
button_timeout = 500 
last_press = [0] * 100 

while True:
    sleep(0.1);
    if (GPIO.input(17) == False ):
		if( last_press[17] + button_timeout < time.time()*1000 ):
			print "pin=17" 
			os.system('mpg123 -q makeit.mp3 &')
			last_press[17] = time.time() * 1000 

    if (GPIO.input(27) == False ):
		if( last_press[27] + button_timeout < time.time()*1000 ):
			print "pin=27" 
			os.system('mpg123 -q workit.mp3 &')
			last_press[27] = time.time() * 1000 		

    




driver = DriverSerial(num = 35*5*3, type = LEDTYPE.WS2811)

#import the bibliopixel base classes
from bibliopixel import *
from bibliopixel.animation import *
class BasicAnimTest(BaseStripAnim):
    def __init__(self, led):
        super(BasicAnimTest, self).__init__(led)
        #do any initialization here

    def step(self, amt = 1):
        for i in range(35*5*3):
            self._led.set(i, colors.hue2rgb((i*4+self._step)%256))
        self._step += amt


#Now try with LEDStrip
led = LEDStrip(driver)

try:
    anim = BasicAnimTest(led)
    anim.run(fps=45)
except KeyboardInterrupt:
    #turn everything off if Ctrl+C is pressed
    led.all_off()
    led.update()