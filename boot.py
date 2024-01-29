#boot.py

import ugit
from machine import Pin
import utime
from microdot import Microdot
import gc

led = Pin("LED", Pin.OUT)

wlan = ugit.wificonnect()
app = Microdot()


@app.route('/')
def index(request):
    return 'Hello'

#@app.route('memory')
#def index(request):
#    response = '<h1>Free Memory={} bytes</hi>'.format(gc.mem_free())
#    return response, {'Content-Type': 'text/html'}

@app.route('toggle')
def index(request):
    led.toggle()
    return "Toggled"

@app.route('update')
def index(request):
    ugit.pull_all()
    return "Updating..."

app.run(port=80)
