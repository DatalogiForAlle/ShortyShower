import hat
import time

speaker = hat.get(hat.SPEAKER)

#variable to change note length
note_length = 10

while True:
    # Increase note length every loop
    note_length = note_length + 10
    print(note_length)

    # Change frequency at certain time steps
    if note_length >= 50:
        speaker.tone(500, note_length)

    if note_length > 100:
        speaker.tone(700, note_length)

    if note_length > 150:
        speaker.tone(1000, note_length)

    if note_length > 200:
        speaker.tone(1800, note_length)



