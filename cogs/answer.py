import discord
from discord.ext import commands
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Answer Ready")

    @commands.command(aliases = ['answer'])
    async def _answer(self,ctx,*,question):
        answers = ['Yes','No','Maybe']
        await ctx.send(f'Q:{question}\nA:{random.choice(answers)}')

def setup(client):
    client.add_cog(Example(client))
