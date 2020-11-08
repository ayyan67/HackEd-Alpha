import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


client.run('Nzc0NzQ4NTI5NTkxNzEzNzky.X6cSyw.IFD58e60AolewrYO3kHaqq6l4ZE')
