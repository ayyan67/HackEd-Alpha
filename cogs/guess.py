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
    async def guess(self,ctx,choice):
        num = random.randint(0,100)
        if num != int(choice):
            await ctx.send(f'My number was {num}, you were {abs(num-int(choice))} off')
        else:
            await ctx.send("Wow! You got it!")



def setup(client):
    client.add_cog(Example(client))
