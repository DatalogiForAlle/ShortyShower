import machine
import time
import dht
import wifi
import requests
import json

sensor = dht.DHT11(machine.Pin(33))

AIO_KEY  = "aio_cSFe38RKUFDWlfbat0VAum28V3RA" #"aio_e8b76f1752f7441f8b01fbd54b94"
FEED_KEY = "humidity"
username = "dybber"
headers = {'X-AIO-Key': AIO_KEY}
url = "https://io.adafruit.com/api/v2/" + username + "/feeds/" + FEED_KEY + "/data/"

while True:
    # Mål luftfugtighed
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed)

    # Forbind til WiFi
    wifi.connect("DIKU1", "PeterNaur")

    # Send data
    data = { "value" : luftfugtighed }
    r = requests.post(url, headers=headers, json=data)
    r.close()

    # Afbryd WiFi forbindelse
    wifi.disconnect()

    # Vent 1 sekund før vi sender datapunkt
    time.sleep_ms(1000)
