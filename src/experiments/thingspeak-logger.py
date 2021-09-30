import machine
import wifi
import time
import dht

sensor = dht.DHT11(machine.Pin(33))

while True:
    # Mål luftfugtighed
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed)

    # Vent 1 sekund inden næste måling
    time.sleep_ms(1000)
