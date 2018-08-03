# imports necessary tools
import asyncio
import discord
import re
import config as cfg

# This is a test for git bash

# actual bot. use shitposter. whatever
shitposter = discord.Client()
regex_shit = re.compile('(\w*)shitpost(\w*)', re.IGNORECASE)
donger_lib = {'lenny': '( ͡° ͜ʖ ͡°)'}
is_donger = False
donger_display = None

lookup_table = {"italy": "Italy? I believe you mean 'Idiot side-switching fettuccine'",
                "me irl": "It's me_irl you heathen fuck",
                "mods are gay": "It is known",
                "kys": "no u",
                "funpost": "Thank you for keeping this a Christian Minecraft server",
                "need a donger": ("Well why didn't you ask me? I am currently compiling the best list of dongers to "
                                  "funpost with. I can give it to you right now. "
                                  "Say it every now and then so you know what dongers I have. "
                                  "Here is what I currently have: \n\n") + "\n".join(donger_lib.keys())}


# on ready
@shitposter.event
async def on_ready():
    print("Houston, we are go. Get your shitposts ready")


# on message, look for and reply to phrase.
@shitposter.event
async def on_message(message):
    if message.author == shitposter.user:
        return

    new_message = message.content.lower()
    if "a gift from the egg gods" in new_message:
        await shitposter.send_message(message.channel, "PRAISE BE!")

    if regex_shit.search(message.content):
        test = regex_shit.search(message.content)
        newstr = '{0}funpost{1}'.format(test.group(1), test.group(2))
        await shitposter.send_message(message.channel, "LANGUAGE. It's " + newstr)

    for key, value in lookup_table.items():
        if key in new_message:
            await shitposter.send_message(message.channel, value)

    if "!donger" in new_message:
        global is_donger
        is_donger = True

    if is_donger:
        keyList = list(donger_lib.keys())
        for i in range(len(keyList)):
            if keyList[i] in new_message:
                donger_display = donger_lib.get(keyList[i])
                break
        if donger_display != None:
            await shitposter.send_message(message.channel, donger_display)


# @shitposter.event
# async def on_reaction_add(reaction, user):
#    if reaction.emoji.id == emoji.doubt:
#        await shitposter.send_message(message.channel, "The statement has been doubted!")


# connects code to bot
shitposter.run(cfg.discord['key'])
