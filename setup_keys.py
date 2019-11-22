#!/usr/bin/env python

import json
import RPi.GPIO as GPIO
import time

from mfrc522 import SimpleMFRC522

# FIXME: make this read from a json file
if __name__ == '__main__':
    reader = SimpleMFRC522()

    with open("keys.json") as f:
        keys = json.load(f)

    print(keys)

    for key in keys.keys():
        try:
            print("\nNow place the tag for \033[1;33m{}\033[0m to write".format(key))
            reader.write(key)
            print("\t \033[1;32mSuccess!\033[0m Wrote {} to tag. Waiting 5 seconds.".format(key))
            time.sleep(5)
        except Exception as e:
            print("Got exception {}".format(repr(e)))

    GPIO.cleanup()
