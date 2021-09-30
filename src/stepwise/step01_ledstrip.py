import machine
import tinkerlib

# 30 LED’er tilsluttet pin 26
ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)

# Indstil LED’ernes farver
ledstrip[0] = (255, 0, 0)
ledstrip[9] = (0, 0, 255)

# Opdater LED’erne ved at kalde ledstrip.write()
ledstrip.write()
