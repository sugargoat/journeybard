#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

import simpleaudio as sa



def play_background():
    filename = 'audio/Underground_Lake.mp3'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing


if __name__ == '__main__':
    reader = SimpleMFRC522()

    welcomed = False

    # Fixme: do this in a separate thread
    play_background()

    while True:
        if not welcomed:
            print("\n~=~=~=~=~=~=~=\nWelcome to the storied pages of the BardGuild. Please present your muse.\n")
            welcomed = True
        try:
            id, text = reader.read()
            print(id)
            print("Ah, the {} has returned. Do tell us of your journey.".format(text.strip()))
            welcomed = False
        except KeyboardInterrupt:
            print("Goodbye!")
            GPIO.cleanup()
            exit()
        except Exception as e:
            print("Unfortunately, we cannot hear the tale of {} at the moment".format(text.strip()))
            welcomed = False
        time.sleep(3)
