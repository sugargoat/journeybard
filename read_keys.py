#!/usr/bin/env python

import json
import RPi.GPIO as GPIO
import random
import subprocess
import time
from mfrc522 import SimpleMFRC522

def random_welcome(bg_pid):
    with open("messages.json") as m:
        messages = json.load(m)
    rand_welcome = random.randint(0, len(messages["welcome"]) - 1)
    print("\n~=~=~=~=~=~=~=\n{}\n".format(messages["welcome"][rand_welcome]))
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/welcome{}.mp3".format(rand_welcome)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def random_muse_response(key, bg_pid):
    with open("messages.json") as m:
        messages = json.load(m)
    rand_muse_response = random.randint(0, len(messages["muse_return"]) - 1)
    print(messages["muse_return"][rand_muse_response].replace('__', key.strip()))
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/muse_return{}{}.mp3".format(key.strip(), rand_muse_response)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def random_tale_response(bg_pid):
    with open("messages.json") as m:
        messages = json.load(m)
    rand_tale_response = random.randint(0, len(messages["tale_response"]) - 1)
    print(messages["tale_response"][rand_tale_response])
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/tale_response{}.mp3".format(rand_tale_response)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def play_background():
    with open("background_music.json") as b:
        bg_music = json.load(b)

    filename = random.choice(list(bg_music.keys()))
    print("Playing ambience from", filename)
    # Call out to OS to play the audio in a new process
    return subprocess.Popen(["mpg123", "audio/background/{}".format(filename)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    reader = SimpleMFRC522()

    welcomed = False

    # Fixme: do this in a separate thread
    bg_pid = play_background()

    while True:
        if not welcomed:
            rw_pid = random_welcome(bg_pid)
            welcomed = True
        try:
            id, text = reader.read()
            print(id)
            random_muse_response(text, bg_pid)
            time.sleep(random.randint(30, 60))
            welcomed = False
        except KeyboardInterrupt:
            print("Goodbye!")
            GPIO.cleanup()
            exit()
        except Exception as e:
            print("Unfortunately, we cannot hear the tale of {} at the moment, due to {}".format(text.strip(), repr(e)))
            welcomed = False
        # Randomly reset to invite people in
        if random.randint(0, 100) < 12:
            welcomed = False
        time.sleep(5)
