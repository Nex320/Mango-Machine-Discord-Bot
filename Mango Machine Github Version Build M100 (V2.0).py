import discord
from discord.ext import commands,tasks
import datetime
import os
import openai
import json
import math
import random
import functools
import itertools
import re
import apiai
import asyncio
import time
from async_timeout import timeout

#Dont forget to install the modules before running!!!!!

#Dont forget to add your tokens / keys

token = "YOUR TOKEN HERE"

openai.api_key = "YOUR KEY HERE"

version = "GithubBuildM100"

status = version + " " + "mango.help"






bot = commands.Bot(command_prefix='mango.', help_command=None, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name = status))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(":warning: Command not found.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":no_entry: Missing required argument.")
    if isinstance(error, commands.TooManyArguments):
        await ctx.send(":no_entry: Too many arguments.")
    else:
        print("Error! please use debugger.")

   
#start of commands



@bot.command()
async def info(ctx):
    print("[INFO] by " + str(datetime.datetime.now()))
    await ctx.send("**Scary internal Info!**")
    await ctx.send("```Mango Machine Github Specific Build```")
    await ctx.send("```Bot version: " + version + "```")
    await ctx.send("```© Hutt innovations.```")



@bot.command()
async def ping(ctx):
    print("[PING] by " + str(datetime.datetime.now()))
    await ctx.send(f"PONG BITCH! Message round-trip took {round(bot.latency * 1000)}ms. What about it?")
    

@bot.command()
async def help(ctx):
    print("[HELP] by " + str(datetime.datetime.now()))
    await ctx.send("**Bot Version: " + version + "\n*Available commands:*\n\nmg.info ```Gives Bot info.```\nmg.ping ```Shows the latency```\nmg.help ```Shows this help screen.```\nmg.ratio ```Please Don't```\nmg.prank ```Funny prank!```\nmg.troll ```Outdated meme that's still relevent```\nmg.funni ```Cog image 42.```\nmg.say ```Make the bot say what you want! Example: \"mg.say bofa deez\"```\nmg.devs ```Shows who is working on the bot.```\nmg.penis ```You get none.```\nmg.pussy ```Still get none.```\nmg.colin ```Mango Machine's Opinions on Colin.```\nmg.corg ```Trolling roach 57```\nmg.nsfw ```Don't Even think about it.```\nmg.mango ```The mango method.```\nmg.cursedmeme ```Shows a cursed sponge bob meme.```\nmg.gpt ```lets you ask the gpt-3 ai questions and whatever. Example: \"mg.gpt Who are you?\"```**")
    
@bot.command()
async def secret(ctx):
    print("[secret] by " + str(datetime.datetime.now()))
    await ctx.send("My dick fell off")
    await ctx.send("https://tenor.com/view/trollge-troll-the-day-of-reckoning-gif-19655212")
    
@bot.command()
async def prank(ctx):
    print("[prank] by " + str(datetime.datetime.now()))
    await ctx.send("https://www.youtube.com/watch?v=qT5zLyKfTyE")
    
@bot.command()
async def troll(ctx):
    print("[troll] by " + str(datetime.datetime.now()))
    await ctx.send("https://cdn.discordapp.com/attachments/914070696374718524/914329895440621569/Trollface_non-free_1.png")

@bot.command()
async def funni(ctx):
    print("[funni] by " + str(datetime.datetime.now()))
    await ctx.send("This is cog.")
    await ctx.send("https://cdn.discordapp.com/attachments/671823406278246410/925773695891431444/unknown.png")
    
@bot.command()
async def ratio(ctx):
    print("[ratio] by " + str(datetime.datetime.now()))
    await ctx.send("NOOOOOOOOOOO")
    await ctx.send("STOP")
    await ctx.send("WHYYYYYYY")
    await ctx.send("A̷̲͌Ȁ̶̱A̸̗͆Ả̸̗A̷̚ͅḀ̴̓A̷̲͌Ȁ̶̱A̸̗͆Ả̸̗A̷̚ͅḀ̴̓")
    await ctx.send("FUCK YOU")
    await ctx.send("https://tenor.com/view/gun-loading-gun-cursed-emoji-mad-gif-24853374")

@bot.command()    
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    print("[say] by " + str(datetime.datetime.now()) + f" \"{text}\"")

    await ctx.send(f"{text}")
    
    
@bot.command()
async def devs(ctx):
    print("[devs] by " + str(datetime.datetime.now()))
    await ctx.send("The Mango Devs: Nex389#8212 & Archimax#1922")
    
@bot.command()
async def penis(ctx):
    print("[penis] by " + str(datetime.datetime.now()))
    await ctx.send("Okay? thats what you get none of.")
    
@bot.command()
async def pussy(ctx):
    print("[pussy] by " + str(datetime.datetime.now()))
    await ctx.send("*umph* sorry, what? i was drowing in it.")

@bot.command()
async def colin(ctx):
    print("[colin] by " + str(datetime.datetime.now()))
    await ctx.send("Tbh hes a bitchass motherfucker, and if hes here right now i have one thing to say.")
    await ctx.send(">bitchass-computer")

@bot.command()
async def corg(ctx):
    print("[corg] by " + str(datetime.datetime.now()))
    await ctx.send("So hot...")
    
@bot.command()
async def nsfw(ctx):
    print("[nsfw] by " + str(datetime.datetime.now()))
    await ctx.send("You sick bastard.")
    await ctx.send("*;)*")
    
@bot.command()
async def mango(ctx):
    print("[mango] by " + str(datetime.datetime.now()))
    await ctx.send("JOE BIDEN JOE BIDEN IOJG$IJPAJKISRHIAHRJ IM A DUMB ASS BITCH")
    await ctx.send("https://cdn.discordapp.com/attachments/914070696374718524/914232509724782653/184150300.png")

@bot.command()    
async def cursedmeme(ctx):
    print("[cursedmeme] by " + str(datetime.datetime.now()))
    await ctx.send("alright here ye go")
    await ctx.send("https://cdn.discordapp.com/attachments/914070696374718524/914232880903880774/video0_7.mov")


@bot.command()    
async def gpt(ctx, *, text):
    message = await ctx.send("`Thinking...`")
    print("[gpt] by " + str(datetime.datetime.now()) + f" Asked GPT: \"{text}\"")

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=text,
    temperature=1,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    response = response['choices'][0]['text']
    
    if response == "":
        await message.edit(content=f":x: `Sorry, The AI Could not make it's mind up.`")
        
    else:
        await message.edit(content=f"{response}")
    
#end of normal commands

    
#Start of risky commands.    
    
  #haha yeah im not putting those in here, if i did you could just ask the bot for its token and shit so yeah no sorry.
    
    
#End of risky commands.



#start of message responder block


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("fuck you"):
        print(f"[Fuck you] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('Fuck you too homie.')
        
    elif message.content.startswith("mango"):
        print(f"[Mango] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('M-M-M-MANGO?!?!??!')
        await message.channel.send('O-OH MY GOD!!!')
        await message.channel.send('SAME DUDE!')
        
    elif message.content.startswith("yada"):
        print(f"[Yada] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('Badoo Burger.')
        
    elif message.content.startswith("man-goes my nuts in your mouth"):
        print(f"[mangoes my nuts in your mouth] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('Shut the fuck up.')
        
    elif message.content.startswith("+help"):
        print(f"[+help] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('fuck yourself fowarding headass')
        
        
    elif message.content.startswith("+8ball"):
        print(f"[+8ball] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('8 balls in your mouth, shut up fowarding bitch.')
    
    elif message.content.startswith("+info"):
        print(f"[+info] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('shut up WARD')
        
    elif message.content.startswith("roach"):
        print(f"[roach] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('https://tenor.com/view/roach-gif-21306135')
        
    elif message.content.startswith("https://www.pornhub.com"):
        print(f"[PH] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('WOAH WOAH HOLD THE FUCK UP BUDDY')
        
    elif message.content.startswith("https://pornhub.com"):
        print(f"[PH] by {message.author} " + str(datetime.datetime.now()))
        await message.channel.send('WOAH WOAH HOLD THE FUCK UP BUDDY')

    await bot.process_commands(message)

#end of message responder block





bot.run(token)
