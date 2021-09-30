import machine
import dht
import time
import hat

# Initialisering af fugtighedssensor
sensor = dht.DHT11(machine.Pin(33))

# Initialisering af højtaler
speaker = hat.get(hat.SPEAKER)

# Variable
timer = 0
tilstand = "INAKTIV"

while True:
    sensor.measure()
    luftfugtighed = sensor.humidity()
    print(luftfugtighed, timer)

    # Skift mellem BAD og INAKTIV baseret på luftfugtighed
    if luftfugtighed >= 80 and tilstand == "INAKTIV":
        tilstand = "BAD"

    if luftfugtighed < 80 and tilstand == "BAD":
        tilstand = "INAKTIV"

    # Tæl timer op når vi er i "BAD"
    if tilstand == "BAD":
        timer= timer +1

    #Alarm går af efter 180 sekunder i bad
    if timer > 180 and tilstand == "BAD":
        tilstand = "ALARM"
        alarm_end_timer = 0

    # Bliv ved at tælle timeren op i ALARM-tilstanden
    if tilstand == "ALARM":
        timer = timer + 1
        speaker.tone(1800, 200)

    #Sluk alarm efter yderligere 5 sekunder
    if timer >= 185:
        timer = 0
        tilstand = "INAKTIV"
    time.sleep_ms(1000)


