import machine
import tinkerlib
import time
import dht

ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 24)
sensor = dht.DHT11(machine.Pin(33))

red = (100, 0, 0)
green = (0, 100, 0)

tilstand = "INAKTIV"
timer = 0

while True:
    # Mål luftfugtighed
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed, timer)

    # Model
    if tilstand == "INAKTIV" and luftfugtighed > 80:
        tilstand = "BAD"

    if tilstand == "BAD" and luftfugtighed < 80:
        tilstand = "INAKTIV"
        timer = 0
    lcd.print(tilstand, lcd.CENTER, 65)

    # View
    if tilstand == "INAKTIV":
        ledstrip.clear()

    if tilstand == "BAD":
        timer = timer + 1
        ledstrip.clear()
        ledstrip.fillN(green, ledstrip.n - timer/10)

    # Vent 1 sekund inden næste måling
    time.sleep_ms(1000)
