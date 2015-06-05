import Adafruit_BBIO.GPIO as GPIO
 
GPIO.setup("P9_12", GPIO.IN)

GPIO.add_event_detect("P9_12", GPIO.FALLING)
#your amazing code here
#detect wherever:

while True : 
    if GPIO.event_detected("P9_12"):
        print "P9_12 - event detected!"
