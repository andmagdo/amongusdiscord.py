
import discord
from sys import exit
import random
import string

# predefine variables
Version = '0.0.1 - using commit 31c0dc0'
guildID = 'test'
lobbyCode = 'test'
auNew = False
result = 0
roomCode = 'Undefined'
# Define client
client = discord.Client()
botToken = "{Bottoken}"


# Define port (8123 is default) (does nothing currently)
port = 8123


# description
description = 'An attempt to replicate the behaviors made by AutoMuteUs.'

#Graceful ctrl c


def startBot():
    print("The current version is " + Version)
    print('Bot is now running.  Press CTRL-C to exit.')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    startBot()

# TODO: to change the command prefix, change .au strings below


@client.event
async def on_message(message):
    upperMessage = message.content
    lowerMessage = str.lower(upperMessage)
    #If the bot writes something that it can be activated by,
    if message.author == client.user:
        return

    elif lowerMessage.startswith('.au'):
        print(lowerMessage)

        await message.delete()

        if lowerMessage == '.au' + ' h' or lowerMessage == '.au' + ' help':
            await message.channel.send("The current version is " + Version + '\n'
                                       'This is in pre-alpha, expect ***Nothing*** to work!\n'
                                       'Among Us Bot command reference:\n'
                                       'Having issues or have suggestions? Join the discord at https://discord.gg/ZkqZSWF !\n'
                                       '`.au help` or `.au h`: Print help info and command usage.\n'
                                       'Below is not yet completed - will throw error\n'
                                       '`.au new` or `.au n`: Start the game in this text channel. Accepts Room code and Region as arguments. Ex: .au new CODE eu. Also works for restarting.\n'
                                       '`.au end` or `.au e`: End the game entirely, and stop tracking players. Unmutes all and resets state.\n'
                                       '`.au track` or `.au t`: Instruct bot to only use the provided voice channel for automute. Ex: `.au t <vc_name>`\n'
                                       '`.au link` or `.au l`: Manually link a player to their in-game name or color. Ex: `.au l @player cyan` or `.au l @player bob`\n'
                                       '`.au force` or `.au f`: Force a transition to a stage if you encounter a problem in the state. Ex: `.au f task or .au f d`(discuss)\n'
                                       )
            print('Command completed successfully')
            return
        elif lowerMessage == '.au' + ' new' or lowerMessage == '.au' + ' n':
            global roomCode
            await message.channel.send('This command is not finished yet! Please refer to `.au help` for a list of finished and unfinished commands')
            embedVar = discord.Embed(title="**You just started a game!**", description="Copy/paste the following link to link your capture:\n  localhost:8123", color=0x00ff00)
            embedVar.add_field(name="Code", value=getRandomString(8), inline=False)
            await message.author.send(embed=embedVar)
            embed = discord.Embed(title="Lobby is Open!",
                                  description="❌ No capture linked! Click the link in your DMs to connect!❌ `" + getRandomString(6),
                                  color=0x00ff40)
            embed.add_field(name="Room Code", value=roomCode, inline=True)
            embed.add_field(name="Region", value="Unprovided", inline=True)
            embed.add_field(name="Tracking", value="Unprovided", inline=True)
            embed.add_field(name="Players Linked", value="0/0", inline=True)
            embed.set_footer(text="React to this message with your in-game color! (or ❌ to leave) ")
            await message.channel.send(embed=embed)
            print('Test Command: ' + lowerMessage)
            return


        elif lowerMessage == '.au' + ' end' or lowerMessage == '.au' + ' e':
            AuEnd()
            await message.channel.send('This command is not finished yet! Please refer to `.au help` for a list of finished and unfinished commands')
            print('Incorrect command: ' + lowerMessage)
            return


        elif lowerMessage == '.au' + ' link' or lowerMessage == '.au' + ' l':
            await message.channel.send('This command is not finished yet! Please refer to `.au help` for a list of finished and unfinished commands')
            print('Incorrect command: ' + lowerMessage)
            return


        elif lowerMessage == '.au' + ' link' or lowerMessage == '.au' + ' l':
            await message.channel.send('This command is not finished yet! Please refer to `.au help` for a list of finished and unfinished commands')
            print('Incorrect command: ' + lowerMessage)
            return


        elif lowerMessage == '.au' + ' track' or lowerMessage == '.au' + ' t':
            await message.channel.send('This command is not finished yet! Please refer to `.au help` for a list of finished and unfinished commands')
            print('Incorrect command: ' + lowerMessage)
            return


        else:
            await message.channel.send('You used this command incorrectly! Please refer to `.au help` for proper command usage')
            print('Incorrect command: ' + lowerMessage)


def getRandomString(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Connect code is:", result_str)
    global result
    result = str.upper(result_str)
    return result


def AuEnd():
    global auNew
    auNew = False
    print('Command failed, not implemented yet')
    return auNew

client.run(botToken)
