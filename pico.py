#pico.py
#from https://github.com/41-6C-61-6E/pico

import machine
import time


###### OTA Updates
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
firmware_url = "https://raw.githubusercontent.com/41-6C-61-6E/pico"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "pico.py")
ota_updater.download_and_install_update_if_available()
######

led = machine.Pin('LED', machine.Pin.OUT) #configure LED Pin as an output pin and create and led object for Pin class

while True:
  led.value(True)  #turn on the LED
  time.sleep(1)   #wait for one second
  led.value(False)  #turn off the LED
  time.sleep(1)   #wait for one second
