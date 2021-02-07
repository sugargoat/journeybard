# journeybard

The goal of this project is to provide an interface for journeyers to present stories, and earn their place among the members of the Journey Bards. Journeyers are encouraged to find muses in the room that may inspire them to take a journey out into the party and collect an adventure. For more lore, see [Lore](#lore), below.

There are 3 phases:

1. [Set Up](#set-up)
1. [Party Initiatialize](#party-initialize)
1. [Maintenance/Updates](#party-maintenance)

# IMPORTANT INFO:

* the login for the pi is `pi` with password `cubegarden`.
* The hostname is `cubedev`, so once you have internet, you can ssh to `pi@cubedev.local`.
* the code is already loaded, and the background music already downloaded at ~/code/journeybard

## Set Up

(All of the set up phase has already been done for the raspberry pi)

1. You will need the following materials:

    * Raspberry pi + power supply + keyboard + monitor
    * Speakers
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

1. Make sure the pi has internet (only necessary to download background music or pull down changes to the repo, not necessary throughout the party)
    * update internet with raspi-config
1. Update the muses list with any found items
1. Register each RFID tag with the associated muse.
1. Download background music and create the "text-to-speech" output
1. Run the interactive program for the party.

## Update Muses Keys File

Add any muses to the json file in [keys.json](keys.json).

## Register Muses with RFID Tags

Run this program to register each of the items onto an RFID tag. The program will print an item on the screen, then tap the corresponding RFID tag to the reader and it will write that string onto the tag.

```
    python3 setup_keys.py
```

### Set Up Audio (Background Music and Text-To-Speech)

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

In general, it should be good-to-go (with the exception of adding muses). The following may be things you want to do in maintenance mode:

    * Address bugs that arise (there will certainly be bugs)
    * Add messages to send people to specific rooms/destinations for certain muses.

## Lore

Here is the additional lore:

### The Story

* Frame story, like Canterbury tales, or Sheherezade and the 1001 nights

### Game Mechanics

The story begins with those who enter.

Once upon a time there was a guild of bards and storytellers, taking on new apprenticeships,. They look at the stories and choose one that appeals to them, or an opject on the wall they choose as a muse.

You will find a way for these stories or muses to send them to other rooms, as apprentice storytellers.

There they will have an adventure, and if they return, and we feel their story worthy, they will be allowed to change one of the stories currently in the book, and move up from apprentice to journeybard.

If they fail to delight us with their adventure take, they can choose to give their apprentice button to someone else, or to try again.

The Journeybard is given a button to recruit an apprentice, and asked to return and tell us the tale. If they impress this time, they become full BardGuild members and are allowed to write a sentence of their choosing on the empty door, telling the story of the RS19 BardGuild.
