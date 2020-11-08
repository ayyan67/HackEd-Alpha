import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ['8ball','test'])
async def _8ball(ctx,*,question):
    responses = ['Yes','No','Maybe','Probably','Hopefully']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx,amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx,member: discord.Member,*, reason = 'None'):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx,member: discord.Member,*, reason = 'None'):
    await member.ban(reason = reason)


client.run('Nzc0NzQ4NTI5NTkxNzEzNzky.X6cSyw.IFD58e60AolewrYO3kHaqq6l4ZE')
