import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

#Load driver for the AllPixel
from bibliopixel.drivers.serial_driver import *
#set number of pixels & LED type here 
driver = DriverSerial(num = 10, type = LEDTYPE.WS2812B)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load channel test animation
from bibliopixel.animation import StripChannelTest
anim = StripChannelTest(led)

try:
	#run the animation
    anim.run()
except KeyboardInterrupt:
	#Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()