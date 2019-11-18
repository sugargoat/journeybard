#!/usr/bin/env python

import json
import os
from gtts import gTTS

if __name__ == '__main__':

    with open("messages.json") as m:
        messages = json.load(m)

    os.makedirs("audio/messages")

    for category, texts in messages:
        for i, text in enumerate(texts):
            tts = gTTS(text)
            tts.save('audio/messages/{}{}.mp3'.format(category, i))
