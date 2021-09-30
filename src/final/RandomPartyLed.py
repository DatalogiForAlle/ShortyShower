import machine
import tinkerlib
import time
import random

#Ledstrip initialisering
ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)

#sort/slukket
color = (0, 0, 0)

while True:
    #Random color selection
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ledstrip[random.randint(0, 29)] = color
    ledstrip[random.randint(0, 29)] = color
    #Turns off the LEDstrip 1 out of 10 times
    if (random.randint(0, 10) == 10):
        ledstrip.clear()
    ledstrip.write()
    time.sleep_ms(10)


