import machine
import time
import dht
import wifi
import requests
import json

# Login oplysninger
username = "dybber"
AIO_KEY  = "aio_cSFe38RKUFDWlfbat0VAum28V3RA" #"aio_6f1752f7441f8b01fbd54b949e3b"

# Kanal/feed på io.adafruit.com vi vil sende til
FEED_KEY = "humidity"

# Hvilken URL vi skal kommunikere med

def send_to_feed(feed, value):
    url = "https://io.adafruit.com/api/v2/"
    url = url + username + "/feeds/" + feed + "/data/"
    headers = {'X-AIO-Key': AIO_KEY}
    data = { "value" : value }
    r = requests.post(url, headers=headers, json=data)
    r.close()

def get_data(feed):
    url = "https://io.adafruit.com/api/v2/"
    url = url + username + "/feeds/" + feed + "/data/last?include=value"
    headers = {'X-AIO-Key': AIO_KEY}
    r = requests.get(url, headers=headers)
    data = r.json()
    r.close()
    if data:
        return data["value"]

while True:
    # Forbind til WiFi
    wifi.connect("DIKU2", "PeterNaur")

    # Send data
    send_to_feed("humidity", 50)

    #a = get_data("humidity")
    #print(a)

    # Afbryd WiFi forbindelse
    wifi.disconnect()

    # Vent 1 sekund før vi sender datapunkt
    time.sleep_ms(1000)
