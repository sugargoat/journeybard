#!/usr/bin/env python

import json
import os
from gtts import gTTS

if __name__ == '__main__':

    # Set up messages
    with open("messages.json") as m:
        messages = json.load(m)

    os.makedirs("audio/messages", exist_ok=True)

    for category, texts in messages.items():
        for i, text in enumerate(texts):
            tts = gTTS(text)
            tts.save('audio/messages/{}{}.mp3'.format(category, i))

    # Set up background music
    with open("background_music.json") as b:
        bg_music = json.load(b)

    os.makedirs("audio/background", exist_ok=True)
    for filename, download_addr in bg_music.items():
        subprocess.Popen(["wget", "--output-document", "audio/background_music/{}".format(filename), download_addr])
