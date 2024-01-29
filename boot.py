
import ugit
from machine import Pin
import utime

ugit.pull_all()

led_onboard = Pin("LED", Pin.OUT)
while True:
 led_onboard.toggle()
 utime.sleep(3)

