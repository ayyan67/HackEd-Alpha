
#import discord package
import os
import random
import asyncio


import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix = '!', intents = intents)

#Functions
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game("HackED Beta"))
    print('Bot is ready')

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx,extension):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):

    await ctx.send(f'Pong')

#Run Client
client.run('NTIxODk4MzcxNTMxOTMxNjYx.XA81vA.KPQmzcfc3N3p6D-FcVJm4ajppgU')
