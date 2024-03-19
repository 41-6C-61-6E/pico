#boot.py
#from https://github.com/41-6C-61-6E/pico/

from time import sleep
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/41-6C-61-6E/pico/main/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "boot.py")
ota_updater.download_and_install_update_if_available()

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

##
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
from machine import Pin
import dht
esp.osdebug(None)
import gc
gc.collect()

#ssid = 'YOUR_SSID'
#password = 'YOUR_PASSWORD'
mqtt_server = '10.10.10.4' #Replace with your MQTT Broker IP

client_id = ubinascii.hexlify(machine.unique_id())
TOPIC_PUB_TEMP = b'esp/dht/temperature'
TOPIC_PUB_HUM = b'esp/dht/humidity'

last_message = 0
message_interval = 5

sensor = dht.DHT22(Pin(4))
#sensor = dht.DHT11(Pin(14))  #if using DHT11, comment the above line and uncomment this line.

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID, PASSWORD)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

##

# Execute main.py
exec(open('main.py').read(), globals())
