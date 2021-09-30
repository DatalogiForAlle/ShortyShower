import machine
import neopixel
import time
import dht

ledstrip = neopixel.NeoPixel(machine.Pin(26), 24)
sensor = dht.DHT11(machine.Pin(33))

def lightN(ledstrip, color, n):
    for i in range(n):
        ledstrip[i] = color
    ledstrip.write()

def clear(ledstrip):
    lightN(ledstrip, (0, 0, 0), ledstrip.n)

red = (100, 0, 0)
green = (0, 100, 0)

tilstand = "VENTER"
timer = 0

while True:
    # Mål luftfugtighed
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed, timer)

    # Model
    if tilstand == "VENTER" and luftfugtighed > 80:
        tilstand = "BAD"

    if tilstand == "BAD" and luftfugtighed < 80:
        tilstand = "VENTER"

    reset_screen()
    lcd.print(tilstand, lcd.CENTER, 65)

    # View
    if tilstand == "VENTER":
        clear(ledstrip)

    if tilstand == "BAD":
        timer = timer + 1
        clear(ledstrip)
        lightN(ledstrip, green, ledstrip.n - timer/10)

    # Vent 1 sekund inden næste måling
    time.sleep_ms(1000)
