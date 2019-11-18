# journeybard

## Set Up

```
    apt-get install mpg123 gTTs
```

Force audio output to headphone jack

```
    amixer cset numid=3 1
    raspi-config
```

Advanced Options > Audio > Force Headphone Jack


## Set Up Audio

This script downloads all the background music specified in background_music.json, and creates speech-to-text for all the phrases in messages.json

```
    setup_audio.py --bg-music --messages
```

## Set up Keys

```
    setup_keys.py
```

## Run the Interactive Program

```
    read_keys.py
```

## References

[Raspberry Pi RFID](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
