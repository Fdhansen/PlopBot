# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
serverName = os.getenv('DISCORD_SERVER_NAME')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=serverName)
    print(f'{client.user} has connected to the Discord Server!')
    print(f'{guild.name}(id: {guild.id})')


    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(token)

#Kan bruges istdet for discord utilities
# for guild in client.guilds:
# if guild.name == serverName:
#  break