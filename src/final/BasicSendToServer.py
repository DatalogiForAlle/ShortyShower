import time
import wifi
import requests
import json
import dht
#connects to a network
#Network name and password has to be inserted
wifi.connect("DIKU2", "PeterNaur")

#Write your own username below
username = "juliusknudsen"
#Write your own key below
AIO_KEY = "aio_LUVS917aFvZoX2cLeyirmh71jRfi"

# Initialisering af fugtighedssensor
sensor = dht.DHT11(machine.Pin(33))

def send_to_feed(feed, value):
    url = "https://io.adafruit.com/api/v2/"
    url = url + username + "/feeds/" + feed + "/data/"
    headers = {'X-AIO-Key': AIO_KEY}
    data = { "value" : value }
    r = requests.post(url, headers=headers, json=data)
    r.close()

#data in the loop will be sent to the server
while True:
    sensor.measure()
    luftfugtighed = sensor.humidity()
    send_to_feed("humidity", luftfugtighed)
    time.sleep_ms(1000)
