import machine
import neopixel
import time
import dht

ledstrip = neopixel.NeoPixel(machine.Pin(26), 8)
sensor = dht.DHT11(machine.Pin(33))

while True:
    # Mål luftfugtighed
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed)

    # Hvor mange LED'er skal tændes?
    antal_led = (luftfugtighed*ledstrip.n)/100

    for i in range(ledstrip.n):
        if i < antal_led:
            ledstrip[i] = (255, 0, 0)
        else:
            ledstrip[i] = (0, 0, 0)
    ledstrip.write()

    # Vent 1 sekund inden næste måling
    time.sleep_ms(1000)
