#imports neccissary tools
import asyncio
import discord
import re

#actual bot. use shitposter. whatever
shitposter = discord.Client()
regexShit = re.compile('(\w*)shitpost(\w*)', re.IGNORECASE)
regexFun = re.compile('(\w*)funpost(\w*)', re.IGNORECASE)

#on ready
@shitposter.event
async def on_ready():
    print("Houstan, we are go. Get your shitposts ready")

#on message, look for and reply to phrase.
@shitposter.event
async def on_message(message):
    if message.author == shitposter.user:
        return
    
    newmessage = message.content.lower()
    if "a gift from the egg gods" in newmessage:
        await shitposter.send_message(message.channel, "PRAISE BE!")

    if regexShit.search(message.content):
        test = regexShit.search(message.content)
        newstr = '{0}funpost{1}'.format(test.group(1), test.group(2))
        await shitposter.send_message(message.channel, "LANGUAGE. It's " + newstr)

    if regexFun.search(message.content):
        await shitposter.send_message(message.channel, "Thank you for keeping this a Christian minecraft server")

    if "italy" in newmessage:
        await shitposter.send_message(message.channel, "Italy? I believe you mean 'Idiot side-switching fettuccine'" )

    if "me irl" in newmessage:
        await shitposter.send_message(message.channel, "It's me_irl you heathen fuck")

    if "mods are gay" in newmessage:
        await shitposter.send_message(message.channel, "It is known")

#@shitposter.event
#async def on_reaction_add(reaction, user):
#    if reaction.emoji.id == emoji.doubt:
#        await shitposter.send_message(message.channel, "The statement has been doubted!")
    

    

#connects code to bot
shitposter.run('NDY1MDExODg0NjM1MTkzMzQ1.DiHT0Q.1WHrZHn18XMgW_1TPNf5WnqKrkA')
    
