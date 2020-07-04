import discord
from discord.ext import commands
import wikipedia
import random

#bot prefix, '+' to initiate bot
bot = commands.Bot(command_prefix = '+')
Token = 'lhS5v9NJ9ebBl2CFbLc0cwCSCFGIuqBj' #See: https://discordapp.com/login?redirect_to=%2Fdevelopers%2Fapplications


#message signifying the bot is online and ready 
@bot.event
async def on_ready():
    print('Bot is ready')


#test command 
@bot.command()
async def scream(context):
        await context.send('AAAAAAAAAHHHHHHHHHHHHHH')


###################
# Smart commands? #
###################

#To produce a title and a link to the wikipedia page of a target  
@bot.command()
async def link(context, *, target):
    target_obj = wikipedia.page(target)
    await context.send(target_obj.title)
    await context.send(target_obj.url)


#scrapes and prints the first two sentences of the target's wiki page 
@bot.command()
async def whatis(context, *, question):
    try:
        await context.send(wikipedia.summary(question, sentences=2))
    except:
        await context.send("Invalid command")


#command to to generate a random joke from list
@bot.command()
async def tellmeajoke(context):
    jokes = ['I was gonna tell a time-traveling joke, but you guys didn’t like it.',
             'What did Mississippi let Delaware? I dont know, but Alaska!',
             'What do you get when you cross a snowman with a vampire?\n Frostbite',
             'What gets wetter the more it dries? A towel',
             'Why cant your nose be 12 inches long?\n Because then it would be a foot!',
             'Why did the robber take a bath before he stole from the bank?\n He wanted to make a clean get away!',
             'I wanted to go on a diet, but I feel like I have way too much on my plate right now',
             'Want to hear a joke about construction? Im still working on it',
             'This graveyard looks overcrowded. People must be dying to get in there.',] #this last one is kinda dark
    try:
        await context.send(f'{random.choice(jokes)}')
    except:
        await context.send("Invalid command")


#runs bot
bot.run("Njk4NzA0MDk2NTQ2MjU5MDA3.XrZM6A.e81uPukByJbzYsfgyr7PLyao18s")
