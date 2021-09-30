import machine
import dht
import time
import tinkerlib

# Fugtighedssensor tilsluttet via pin 33 (gul ledning)
ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)
sensor = dht.DHT11(machine.Pin(33))

green = (0, 255, 0)
red = (255, 0, 0)
tilstand = "INAKTIV"

while True:
    sensor.measure()                  # 1) Foretag måling
    luftfugtighed = sensor.humidity() # 2) Gem luftfugtighed i variabel
    print(luftfugtighed)              # 3) Vis den aflæste værdi
    time.sleep_ms(1000)

    color = green
    if luftfugtighed > 80 and tilstand == "INAKTIV":
        color = red
        tilstand = "BAD"
    ledstrip.fillN(color, luftfugtighed*3/10)
