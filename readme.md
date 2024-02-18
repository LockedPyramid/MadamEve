# Documentation

## Program description

Use the Janice API through Discord

Developed by Locked Pyramid

Built for the EVE Online corporation **Gjallarhorn Incorporated**

## Use of the bot by users

Start off all commands with ```!```

### Base commands

To make a purchase order to Yvftu, use: ```sell``` + Items

Example:

```
!sell crokite 1000
veldspar 1000
crystalline crokite 1000
crokite 10000
crokite 100000
```

To get 100% Jita values, use ```Jita``` + Items
```
!Jita crokite 1000
veldspar 1000
crystalline crokite 1000
crokite 10000
crokite 100000
```

### Advanced commands

To call Janice for regular items, use: ```Price``` + [Market] + [Percentage of price] + Items

Example:

```
!Price 2 100 crokite 1000
veldspar 1000
crystalline crokite 1000
crokite 10000
crokite 100000
```

To repo items, use:  ```Repo``` + [Market] + [Price percent] + [Ore eff] + Items

Example:

```
!Repo 2 93 82.93 crokite 1000
veldspar 1000
crystalline crokite 1000
crokite 10000
crokite 100000
```

To get just the buying price and to repo your items use: ```RepoBuy``` + [Market] + [Market Percentage] + [Ore eff] + Items

Example:

```
!RepoBuy 2 93 82.93 crokite 1000
veldspar 1000
crystalline crokite 1000
crokite 10000
crokite 100000
```

## Setting up the bot

| Please keep in mind that I am not responsible for this code once it is in your hands, everything you do is at your own risk and does not have any warranties as per the license. Please follow these steps with a grain of salt, these are my experiences on my own machine, and are designed for a debian based operating system. **I AM NOT RESPONSIBLE WHAT YOU DO ON YOUR OWN MACHINE** 

This is assuming you have already created a discord bot for your server and you need the back end.
1. Download the repository from Github onto a server of your choice, for this demonstration I will be using a Debian based server.
2. Make [MadamRunner.sh](MadamRunner.sh) an executable
3. Set up a service that calls [MadamRunner.sh](MadamRunner.sh) on boot of the server
4. Run [bot.py](bot.py) to initialize the Discord.key and Janice.key files, this will create an error, that is fine. 
5. Paste your keys into their respective files: [Discord.key](/Storage/Discord.key) and [Janice.key](/Storage/Janice.key). To obtain a Janice API key, contact kukkino on Discord
6. Go to [setting](settings.py) and change your file locations in respect to their real locations on your machine
    - The current file locations are the ones on my Debian server
    - If you were wondering, ```ada``` is the name of a D&D Character I played a while back
7. Change the messages on [bot.py](bot.py) if you wish
8. reboot your machine and have fun!
-------------

Fly safe o7
