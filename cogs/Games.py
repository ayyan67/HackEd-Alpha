import discord
from discord.ext import commands
import random
import asyncio


intents = discord.Intents.default()
intents.members = True
intents.reactions = True

class Games(commands.Cog):

    def __init__(self,client):
        self.client = client

#events
    @commands.Cog.listener()

    async def on_ready(self):
            print('Games Loaded!')

    
           

    
    
#commands
    @commands.command()
    async def RPS(self,ctx):

        emojis = ['🌑', '📃', '✂']

        botC = random.choice(emojis)
        
        print(botC)

        message = await ctx.send('Choose an action!')

        for x in emojis:
                await message.add_reaction(x)

        def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in emojis

        try:
            reaction,user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Time's up! You LOSE")
        else:
            if str(reaction.emoji) == emojis[0] and botC == emojis[0]:
                await ctx.send("I chose ROCK. It's a tie I guess...")
                return
            elif str(reaction.emoji) == emojis[0] and botC == emojis[1]:
                await ctx.send("I chose PAPER. You LOSE")
                return

            elif str(reaction.emoji) == emojis[0] and botC == emojis[2]:
                 await ctx.send("I chose SCISSORS. You WIN")
                 return

            if str(reaction.emoji) == emojis[1] and botC == emojis[0]:
                await ctx.send("I chose ROCK. You WIN")
                return
            
            elif str(reaction.emoji) == emojis[1] and botC == emojis[1]:
                await ctx.send("I chose PAPER. It's a tie I guess...")
                return
               
            elif str(reaction.emoji) == emojis[1] and botC == emojis[2]:
                 await ctx.send("I chose SCISSORS. You LOSE")
                 return

            if str(reaction.emoji) == emojis[2] and botC == emojis[0]:
                await ctx.send("I chose ROCK. You LOSE")
                return
            
            elif str(reaction.emoji) == emojis[2] and botC == emojis[1]:
                await ctx.send("I chose PAPER. You WIN")
                return
               
            elif str(reaction.emoji) == emojis[2] and botC == emojis[2]:
                 await ctx.send("I chose SCISSORS. It's a tie I guess...")
                 return

            


       


        

                
        




        
        


    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx, *, question):
                responses = ["It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
                await ctx.send(f'{random.choice(responses)}')


    ###########




def setup(client):
    client.add_cog(Games(client))
