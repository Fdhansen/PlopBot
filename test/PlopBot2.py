import os
import random
import hasblib
from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='Potato', help='What a useless command')
async def kartoffel(ctx):
    messagetosend = 'Potatoes? Then it have to be fries!'
    await ctx.send(messagetosend)


@bot.command(name='dice', help='Rolls the dice?')
async def roll(ctx, number_of_dice: int):
    message = 'You rolled a :'
    dice = [str(random.choice(range(1, 7)))
            for _ in range(number_of_dice)]
    await ctx.send(message + "\n" + ', '.join(dice))


@bot.command(name='join', help="Makes the bot join your vchat")
async def join(ctx):
    message = "I have joined the voice chat.. dunno why though"
    channel = ctx.author.voice.channel
    await channel.connect()
    ctx.send(message)

@bot.command(name='potato', help="Makes the bot go potato");
async def potato(ctx):
    message = "I am potato"
    channel = ctx.author.voice.channel
    await channel.connect()
    ctx.send(message)

async def potato(ctx):
    potato = hashlib.md5(b'potatolovingforreal')
    print(potato)
    dingo = random.choice(range(1,7))
    print(dingo)

async def potato(ctx):
    potato = hashlib.md5(b'potatolovingforreal')
    print(potato)
    dingo = random.choice(range(1,7))
    print(dingo)

async def potato(ctx):
    potato = hashlib.md5(b'potatolovingforreal')
    print(potato)
    dingo = random.choice(range(1,7))
    print(dingo)


async def potato(ctx):
    potato = hashlib.md5(b'potatolovingforreal')
    print(potato)
    dingo = random.choice(range(1,7))
    print(dingo)

bot.run(token)
