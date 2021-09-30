import machine
import neopixel
import time
import dht
import wifi
import requests
import json

ledstrip = neopixel.NeoPixel(machine.Pin(26), 8)
sensor = dht.DHT11(machine.Pin(33))

API_KEY = "4f27a424b7add9581fe615fcf25a6256129e865185"
FEED_ID = "157953029969771630"
headers = headers = {'api-key': API_KEY}
iotplotterRequestUrl = "http://iotplotter.com/api/v2/feed/" + FEED_ID

# Alternatives: Emitter.io, Phant (https://github.com/sparkfun/phant), Gweet, Xively, AskSensors

while True:
    # Mål luftfugtighed
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed)

    wifi.connect("DIKU 1", "PeterNaur")
    response = requests.get("http://dweet.io/dweet/for/shortyshower?humidity=" + str(luftfugtighed))
    # View: https://dweet.io/follow/shortyshower

    data = { "data" : { "Humidity" : [{ "value" : luftfugtighed }]}}
    print(json.dumps(data))
    print(iotplotterRequestUrl)
    r = requests.post(iotplotterRequestUrl,
                      headers=headers,
                      json=data)

    wifi.disconnect()
    time.sleep_ms(1000)
