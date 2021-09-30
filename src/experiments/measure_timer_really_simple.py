import machine
import dht
import time
import tinkerlib

ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)
red = (100, 0, 0)
green = (0, 100, 0)

# Fugtighedssensor tilsluttet via pin 33 (gul ledning)
sensor = dht.DHT11(machine.Pin(33))

# Initialiser timer
timer = 0

while True:
    sensor.measure()                  # 1) Foretag måling
    luftfugtighed = sensor.humidity() # 2) Gem luftfugtighed i variabel
    print(luftfugtighed, timer)       # 3) Vis den aflæste værdi + timer

    if luftfugtighed > 80:
        timer = timer + 1
    else:
        timer = 0

    ledstrip.clear()
    ledstrip.fillN(red, 5 - timer//10)

    time.sleep_ms(1000)               # 4) Vent 1 sekund

