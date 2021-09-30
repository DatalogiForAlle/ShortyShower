import machine
import dht
import time
import tinkerlib

ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)
red = (100, 0, 0)
green = (0, 100, 0)

#ledstrip.clear()

# Fugtighedssensor tilsluttet via pin 33 (gul ledning)
sensor = dht.DHT11(machine.Pin(33))

timer = 0

while True:
    sensor.measure()                  # 1) Foretag måling
    luftfugtighed = sensor.humidity() # 2) Gem luftfugtighed i variabel
    print(timer)              # 3) Vis den aflæste værdi

    if luftfugtighed > 80:
        timer = timer + 1
    else:
        timer = 0

    time.sleep_ms(1000)
