import machine
import dht
import time
import tinkerlib

ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)
red = (100, 0, 0)
green = (0, 100, 0)

# Fugtighedssensor tilsluttet via pin 33 (gul ledning)
sensor = dht.DHT11(machine.Pin(33))

while True:
    sensor.measure()                  # 1) Foretag måling
    luftfugtighed = sensor.humidity() # 2) Gem luftfugtighed i variabel
    print(luftfugtighed)              # 3) Vis den aflæste værdi

    if luftfugtighed > 80:
        ledstrip.fillN(red, luftfugtighed*3/10)
    else:
        ledstrip.fillN(green, luftfugtighed*3/10)

    time.sleep_ms(1000)
