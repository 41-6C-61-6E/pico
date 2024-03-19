#main.py
#from https://github.com/41-6C-61-6E/pico

def connect_mqtt():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server)

  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
      sensor.measure()
      temp = sensor.temperature()
      hum = sensor.humidity()
      temp = (b'{0:3.1f}'.format(temp))
      hum =  (b'{0:3.1f}'.format(hum))
      print('Temperature: %s' %temp, 'Humidity: %s' %hum)
      client.publish(TOPIC_PUB_TEMP, temp)
      print('Published message %s to topic %s' %(temp,TOPIC_PUB_TEMP))
      client.publish(TOPIC_PUB_HUM, hum)
      print('Published message %s to topic %s' %(hum,TOPIC_PUB_HUM))
      print()
      last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
