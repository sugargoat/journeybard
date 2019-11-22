# journeybard

The goal of this project is to provide an interface for journeyers to present stories, and earn their place among the members of the Journey Bards. Journeryers are encouraged to find muses in the room that may inspire them to take a journey out into the party and collect an adventure. For more lore, see [Lore](#lore), below.

There are 2 phases:

1. [Set Up](#set-up)
1. [Party Initiatialize](#party-initialize)
1. [Maintenance/Updates](#party-maintenance)

Most of the set up phase has been done for the raspberry pi

## Set Up

1. You will need the following materials:

    * raspberry pii
    * RFID reader
    * female-to-female jumper cables
    * soldering kit for RFID reader
    * RFID tags (13.56 MHz)
    * "Muse" items

1. Solder RFID connectors and use female-female jumper cables to connect the RFID reader to the raspberry pi, using the schematic here: [Raspberry Pi RFID](https://pimylifeup.com/raspberry-pi-rfid-rc522/)

1. Set up environment on the raspberry pi for RFID python libraries (also outlined here: [Raspberry Pi RFID](https://pimylifeup.com/raspberry-pi-rfid-rc522/))

1. Install packages for playing audio and text-to-speech

```
    apt-get install mpg123 gTTs
```

1. Force audio output to headphone jack and connect speakers.

```
    amixer cset numid=3 1
    raspi-config
```

Select: Advanced Options > Audio > Force Headphone Jack

# Party Initialize

To get ready for the party, you will need to:

1. Make sure the pi has internet
1. Update the muses list with any found items, then register each RFID tag with the associated muse.
1. Download background music and create the "text-to-speech" output
1. Run the interactive program for the party.

## Update Muses Keys File

Add any muses to the json file in [keys.json](keys.json).

## Set up Keys

Run this program to register each of the items onto an RFID tag. The program will print an item on the screen, then tap the corresponding RFID tag to the reader and it will write that string onto the tag.

```
    python3 setup_keys.py
```

### Set Up Audio

This script downloads all the background music specified in [background_music.json](background_music.json), and creates speech-to-text for all the phrases in [messages.json](messages.json), with the keys from the keys.json file subbed in.

Please use your creativity and humor to add additional messages to [messages.json](messages.json). This makes the JourneyBard portal seem more dynamic and interesting.

If you want to add additional background music, you can edit the [background_music.json](background_music.json) file. All of the music is currently downloaded onto the pi. Note: if you don't want to re-download the music, do not provide `--bg-music` to the setup_audio.py script.

```
    python3 setup_audio.py --bg-music --messages
```

## Run the Interactive Program

Now you're ready to play! Just run the below:

```
    python3 read_keys.py
```

## Party Maintenance

In general, it should be good-to-go. The following may be things you want to do in maintenance mode:

    * Address bugs that arise (there will certainly be bugs)
    * Add messages to send people to specific rooms/destinations for certain muses.
