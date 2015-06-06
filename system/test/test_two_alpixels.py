from bibliopixel.led import *
from bibliopixel.drivers.serial_driver import *
import bibliopixel.colors as colors

driverA = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 2)
driverB = DriverSerial(LEDTYPE.WS2811, 32*5*4, deviceID = 1)

led = LEDStrip([driverA, driverB])


for i in range(2*32*5*4):
#    led.fill(colors.Red, 0, i)   
    led.fill(colors.hue2rgb(i%256), 0, i)   
    led.update()
