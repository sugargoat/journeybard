#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


if __name__ == '__main__':
    reader = SimpleMFRC522()

    try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
    finally:
        GPIO.cleanup()
