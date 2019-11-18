#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

while True:
    try:
        id, text = reader.read()
        print(id)
        print("Ah, the {} has returned. Do tell us of your journey.".format(text))
    except Exception as e:
        print("Unfortunately, we cannot hear the tale of {} at the moment".format(text))
    time.sleep(3)

GPIO.cleanup()
