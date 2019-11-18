#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

welcomed = False

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
    except Exception as e:
        print("Unfortunately, we cannot hear the tale of {} at the moment".format(text.strip()))
        welcomed = False
    time.sleep(3)
