#!/usr/bin/env python

import json
import os
import subprocess
import sys
from gtts import gTTS

if __name__ == '__main__':

    if '--messages' in sys.argv:
        print("Now setting up audio for voice messages")
        with open("messages.json") as m:
            messages = json.load(m)

        with open("keys.json") as k:
            keys = json.load(k)

        with open("destinations.json") as k:
            keys = json.load(k)

        os.makedirs("audio/messages", exist_ok=True)

        for category, texts in messages.items():
            for i, text in enumerate(texts):
                if '__' in text:
                    for key, destination in keys:
                        text = text.replace('__', key).replace('_', ' ').replace('**', destination)
                        tts = gTTS(text)
                        tts.save('audio/messages/{}{}{}.mp3'.format(category, key, i))
                else:
                    tts = gTTS(text)
                    tts.save('audio/messages/{}{}.mp3'.format(category, i))

    if '--bg-music' in sys.argv:
        print("Now setting up audio for background music")
        with open("background_music.json") as b:
            bg_music = json.load(b)

        os.makedirs("audio/background", exist_ok=True)
        for filename, download_addr in bg_music.items():
            subprocess.Popen(["wget", "--output-document", "audio/background/{}".format(filename), download_addr])
