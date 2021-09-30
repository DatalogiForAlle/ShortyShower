import machine
import tinkerlib
import time
ledstrip = tinkerlib.LEDStrip(machine.Pin(26), 30)

red = (255, 0, 0)
blue = (0, 0, 255)

# Tænd den første diode
ledstrip[0] = red
ledstrip.write()
time.sleep_ms(200)

ledstrip[1] = blue
ledstrip.write()
time.sleep_ms(200)

ledstrip[2] = red
ledstrip.write()
time.sleep_ms(200)

ledstrip[3] = blue
ledstrip.write()
time.sleep_ms(200)

ledstrip[4] = red
ledstrip.write()
time.sleep_ms(200)

ledstrip[5] = blue
ledstrip.write()
time.sleep_ms(200)

ledstrip[6] = red
ledstrip.write()
time.sleep_ms(200)

ledstrip[7] = blue
ledstrip.write()
time.sleep_ms(200)
