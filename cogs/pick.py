import discord
from discord.ext import commands
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Pick Ready")

    @commands.command()
    async def pick(self,ctx,*,choices):
        stuff = choices.split()
        await ctx.send(f'{random.choice(stuff)} seems like a good option.')

def setup(client):
    client.add_cog(Example(client))
