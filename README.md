# Get the official working version at [AutoMuteUs](https://github.com/denverquane/automuteus) Made by [DenverQuane](https://github.com/denverquane)
# AmongUsAutoMute.py (Pre-Alpha) 

Discord Bot to harness Among Us game data, and automatically mute/unmute players during the course of the game!

Works in conjunction with [amonguscapture](https://github.com/denverquane/amonguscapture)

**This program is in Pre-Alpha. While we are working on making this work, IT WILL NOT WORK**

Have any questions, concerns, bug reports, or just want to chat? Join the discord at https://discord.gg/ZkqZSWF Then Dm or ping @andmagdo#2803 

# Requirements

1. This program should run on any device that supports python and pip.
2. You need a minimum of 12 open emoji slots on your server. The bot uses player emojis to link discord users to in-game player colors; it will add them automatically, but you need at least 12 slots (25 recommended).
3. You must run the discord bot, and the capture portion (See Easiest installation below) at the same time. Easiest installation covers running the bot
portion locally, but feel free to use Heroku or Docker or the like to host the bot remotely.


# Installation

See the
Usage/Commands sections below! Follow all the instructions below instead.

## Pre-Installation Steps, Important!!!
1. Create an Application and Bot account for your Discord Server (requires Admin privileges on the Server in question).

Now follow either the `Easiest` install, or the `Install From Source`:

## Before Installing:
Make sure both Python3 and pip3 is installed (Type python3 into a terminal to find out)
(Windows Install) https://www.python.org/downloads/windows/ Make sure you are picking latest python3.
Linux should have it already installed, but if not (somehow), use your distro's package manager to install python3 and python3-pip
Incase that pip isn't installed, do python3 get-pip.py
Once you have pip installed, do pip3 install --upgrade pip
## If this doesnt work on Windows, replace pip below with `py -3 -m pip install -U {package}`

## Installing dependencies
Run the following commands:
pip3 install discord.py
pip3 install string
pip3 install random



The bottom 2 should already be installed.


## Easiest:
1. [Download the latest release python file (`.py`)](https://github.com/andmagdo/amongusdiscord.py/releases) for this discord bot.
2. Edit the .py in a text editor of your choice and add your bot token (In the quotes)
3. Run the executable from step 1, either by using `Python {nameOfFile.py}` in a terminal window.
4. [Download the latest `amonguscapture.exe`](https://github.com/denverquane/amonguscapture/releases). If you are running the Discord bot remotely,
you can add a `host.txt` file in the same folder with the contents `http://<host>:<port>` to point to that instance, but this is totally optional.
5. **If Among Us is already running,** then start the capture executable you downloaded in the previous step. Otherwise, start the game and **then** start the capture.

Congrats, if you followed the instructions correctly, the bot should now be running! See the Sample Usage section below for details.

# Sample Usage
### CURRENTLY, NONE OF THESE COMMANDS HAVE FUNCTION. THEY MAY LOOK REAL, BUT HAVE NO EFFECT
To start the bot in the current channel, type the following `.au` command in Discord:
```
.au new
# Starts a game, and allows users to react to emojis to link to their in-game players
```
Get Playing!

If you want to view command usage or see the available options, type `.au` or `.au help` in your Discord channel.

If you need to add more players to the tracking list, they can be added using the reaction emojis once back in the lobby. Or, manually using `.au link @player color`.

# Bot Commands
The Discord Bot uses the `.au` prefix for any commands

|Command| Alias | Arguments | Description | Example |
|---|---|---|---|---|
|`.au help`|`.au h`|None|Print help info and command usage||
|`.au new`|`.au n`|None|Start a new game in the current text channel. Optionally accepts the room code and region|`.au n CODE eu`|
|`.au track`|`.au t`|VC Name|Tell Bot to use a single voice channel for mute/unmute, and ignore any other channels|`.au t Test Voice`|
|`.au link`|`.au l`|@name color|Manually link a discord user to their in-game color|`.au l @Soup cyan`|
|`.au refresh`|`.au r`|None|Remake the bot's status message entirely, in case it ends up too far up in the chat.||
|`.au end`|`.au e`|None|End the game entirely, and stop tracking players. Unmutes all and resets state||
|`.au unlink`|`.au u`|@name|Manually unlink a player|`.au u @player`|
|`.au settings`|`.au s`||View and change settings for the bot, such as the command prefix or mute behavior||
|`.au force`|`.au f`|stage|Force a transition to a stage if you encounter a problem in the state|`.au f task` or `.au f d`(discuss)|
|`.au pause`|`.au p`||Pause the bot, and don't let it automute anyone until unpaused. **will not un-mute muted players, be careful!**||

# Similar Projects

- [AmongUsDiscord](https://github.com/denverquane/amongusdiscord): Without their original go program (and the fact that I want dev on their discord server) I never would have even considered this. Most definitly better than this and better maintained

- [AmongUsBot](https://github.com/alpharaoh/AmongUsBot): Without their original Python program
with a lot of the OCR/Discord functionality, DenverQuane never would have even thought of this idea! Not currently maintained

- [amongcord](https://github.com/pedrofracassi/amongcord): A great program for tracking player status and auto mute/unmute in Among Us.
Their project works like a traditional Discord bot; very easy installation!

- [Silence Among Us](https://github.com/tanndev/silence-among-us#silence-among-us): Another bot quite similar to this one, which also uses AmongUsCapture. Now in early-access with a publicly-hosted instance.

# Troubleshooting
### YET AGAIN: CURRENTLY, NONE OF THE COMMANDS HAVE FUNCTION. THEY MAY LOOK REAL, BUT HAVE NO EFFECT, NONE OF THESE TROUBLESHOOTING STEPS WILL BE USED CURRENTLTY

- **"Websocket 400-something: Authentication Failed" Error!**
Your `DISCORD_BOT_TOKEN` is incorrect or invalid. Make sure you copied/pasted the Bot *token*, NOT the "client secret" from the Discord Developer portal

- **"Emoji ID is not a snowflake" Error! Or the bot doesn't provide emojis as reactions on the status message!**
The discord API is agonizingly slow to upload new emojis, inform bots about the presence of new/updated emojis, and delete emojis.
The easiest answer is to **give it a while** (sometimes can take almost 30 minutes), and try again.


