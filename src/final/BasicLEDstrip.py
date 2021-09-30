import machine
import tinkerlib

# 30 LED’er tilsluttet pin 26
ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)

#farver
Red = (255, 0, 0)
Blue = (0, 0, 255)
Grøn = (0, 255, 0)
Gul = (255, 255, 0)
Lilla = (127, 0, 255)
Tyrkis = (0, 255, 255)


for i in range(30):
    ledstrip[i] = (255, 0, 0)
    time.sleep_ms(200) # Vent 200 millisekunder
    ledstrip.write()

