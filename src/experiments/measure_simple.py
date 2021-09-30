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

    if luftfugtighed > 80:
        ledstrip[0] = (255, 0, 0)
        ledstrip[1] = (255, 0, 0)
        ledstrip[2] = (255, 0, 0)
        ledstrip[3] = (255, 0, 0)
        ledstrip[4] = (255, 0, 0)
        ledstrip[5] = (255, 0, 0)
        ledstrip[6] = (255, 0, 0)
        ledstrip[7] = (255, 0, 0)
    else:
        ledstrip[0] = (0, 100, 0)
        ledstrip[1] = (0, 100, 0)
        ledstrip[2] = (0, 100, 0)
        ledstrip[3] = (0, 100, 0)
        ledstrip[4] = (0, 100, 0)
        ledstrip[5] = (0, 100, 0)
        ledstrip[6] = (0, 100, 0)
        ledstrip[7] = (0, 100, 0)
    ledstrip.write()

    # Vent 1 sekund inden næste måling
    time.sleep_ms(1000)
