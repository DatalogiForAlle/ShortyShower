import machine
import time
import dht
import wifi
import tinkerlib

#sensor = dht.DHT11(machine.Pin(33))

client = tinkerlib.AdafruitIO("aio_cSFe38RKUFDWlfbat0VAum28V3RA", "dybber")

while True:
    # Mål luftfugtighed
    #sensor.measure()
    #luftfugtighed = sensor.humidity()
    #print(luftfugtighed)

    wifi.connect("DIKU1", "PeterNaur")

    #client.emit("humidity", luftfugtighed)
    v = client.read("humidity")
    print("Return: " + str(v))

    time.sleep_ms(1000)
