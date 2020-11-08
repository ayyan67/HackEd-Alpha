import discord
from discord.ext import commands
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Guess Ready")

    @commands.command()
    async def guess(self,ctx):
        await ctx.send("Pick a number from 0-100:")


def setup(client):
    client.add_cog(Example(client))
