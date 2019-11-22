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
    print("\n\t\t\t\t~=~=~=~=~=~=~=\n{}\n".format(messages["welcome"][rand_welcome]))
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/welcome_{}.mp3".format(rand_welcome)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def random_muse_response(key, bg_pid):
    with open("messages.json") as m:
        messages = json.load(m)
    rand_muse_response = random.randint(0, len(messages["muse_return"]) - 1)
    print(messages["muse_return"][rand_muse_response].replace('__', key.strip()).replace('_', ' '))
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/muse_return_{}_{}.mp3".format(key.strip(), rand_muse_response)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def random_tale_response(bg_pid):
    with open("messages.json") as m:
        messages = json.load(m)
    rand_tale_response = random.randint(0, len(messages["tale_response"]) - 1)
    print(messages["tale_response"][rand_tale_response])
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/tale_response_{}.mp3".format(rand_tale_response)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def play_background():
    with open("background_music.json") as b:
        bg_music = json.load(b)

    filename = random.choice(list(bg_music.keys()))
    print("Playing ambience from", filename.strip('.mp3'))
    # Call out to OS to play the audio in a new process
    return subprocess.Popen(["mpg123", "audio/background/{}".format(filename)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def journey_prompt(key, bg_pid):
    with open("messages.json") as m:
        messages = json.load(m)
    with open("keys.json") as k:
        keys = json.load(k)
    rand_journey_prompt = random.randint(0, len(messages["journey_prompt"]) - 1)
    print(messages["journey_prompt"][rand_journey_prompt].replace('__', key.strip()).replace('_', ' ').replace('**', keys[key.strip()]))
    bg_pid.kill()
    return subprocess.Popen(["mpg123", "audio/messages/journey_prompt_{}_{}.mp3".format(key.strip(), rand_journey_prompt)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    reader = SimpleMFRC522()

    # Fixme: do this in a separate thread
    bg_pid = play_background()

    out_muses = set()

    while True:
        try:
            # FIXME: Should use an IR sensor to play welcome when people approach
            rw_pid = random_welcome(bg_pid)
            # Read continuously until an RFID tag is presented
            id, text = reader.read()
            print(id)
            print("current out muses = ", out_muses)

            if text in out_muses:
                print('The muse has returned!')
                random_muse_response(text, bg_pid)
                out_muses.delete(text)
                # Sleep while the journeyer either relays a story, or wanders off
                time.sleep(random.randint(30, 60))
            else:
                print('This muse is about to go out')
                journey_prompt(text, bg_pid)
                out_muses.add(text.strip())
                time.sleep(8)

        except KeyboardInterrupt:
            print("Goodbye!")
            GPIO.cleanup()
            exit()
        except Exception as e:
            print("Unfortunately, we cannot hear the tale of {} at the moment, due to {}".format(text.strip(), repr(e)))
        time.sleep(5)
