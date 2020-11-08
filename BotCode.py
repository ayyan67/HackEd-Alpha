import discord
from discord.ext import commands
import os

<<<<<<< HEAD
client = commands.Bot(command_prefix = ".")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Nzc0NzQ4NTI5NTkxNzEzNzky.X6cSyw.IFD58e60AolewrYO3kHaqq6l4ZE')
=======
# Makes the Bot go online
client = discord.Client()

# yooo
# Andrew
>>>>>>> origin/Ayyan
