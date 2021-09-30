import dht
import machine
#import neopixel
import time
from tinkerlib import Buzzer, ADKeypad
#import ssd1306


#i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
#pin36 = machine.Pin(36, mode=machine.Pin.IN)
#lcd = ssd1306.SSD1306_I2C(128,64,i2c)
buzzer = Buzzer(machine.Pin(26), dutycycle_in_percent=True)
buzzer.noTone()
quarter_note = 100
#ledstrip = neopixel.NeoPixel(machine.Pin(12), 8)
#ledstrip2 = neopixel.NeoPixel(machine.Pin(26), 8)
d = dht.DHT22(machine.Pin(33))

lcd.setRotation(1)


tilstand = "deaktiveret"
off = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green=(0, 255, 0)
green2=(32, 218, 0)
yellow1=(75, 180, 0)
yellow2=(100, 150, 0)
yellow3=(255, 255, 0)
yellow4=(154, 96, 0)
yellow5=(186, 64, 0)
red2=(218, 32, 0)
colorlist=(green,green2,yellow2,yellow3,yellow4,yellow5,red2,red)
color = colorlist

#d.measure
#d.temperture eg. 23 (C)
#d.humidity eg. 41.3 (% RH)




#if dt >= 41:
    #print("too hot")
    #for f in range(30):
    #    ledstrip[f] = red
    #ledstrip.write()

def keypadButtonDown(key):
    global tilstand
    global timer
    if key == 0 and tilstand == "alarm":

        tilstand = "snooze"
        timer = 0


#keypad = ADKeypad(pin36, button_down=keypadButtonDown)


while True:
    buzzer.noTone()
    d.measure()
    dh = d.humidity()
    print(dh)
    if tilstand == "deaktiveret":
        timer = 0
        if dh >= 80:
            tilstand = "aktiv"
    if tilstand == "aktiv":
        timer = timer + 1000
    if tilstand == "aktiv" and timer == 7000:
        tilstand = "alarm"
    if tilstand == "alarm":
        buzzer.tone(2637, quarter_note)
    if tilstand != "deaktiveret" and dh < 80:
        tilstand = "deaktiveret"

    lcd.clear(lcd.BLACK)
    lcd.print(str(dh)+"% luftfugtighed",0,0)
    lcd.print(tilstand,0,16)
    lcd.print(str(timer/1000)+"sek",0,30)
    #lcd.show()
    time.sleep_ms(1000)
    #clear(ledstrip)
    #clear(ledstrip2)

