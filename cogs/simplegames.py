import discord
from discord.ext import commands
import random

class SimpleGames(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Simple Games Ready")

    @commands.command()
    async def guess(self,ctx,choice):
        num = random.randint(0,100)
        if num != int(choice):
            await ctx.send(f'My number was {num}, you were {abs(num-int(choice))} off')
        else:
            await ctx.send("Wow! You got it!")

    @commands.command()
    async def pick(self,ctx,*,choices):
        stuff = choices.split()
        await ctx.send(f'{random.choice(stuff)} seems like a good option.')

    @commands.command()
    async def answer(self,ctx,*,question):
        answers = ['Yes','No','Maybe']
        await ctx.send(f'Q:{question}\nA:{random.choice(answers)}')

def setup(client):
    client.add_cog(SimpleGames(client))