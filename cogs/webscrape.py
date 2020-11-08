import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class webCommands(commands.Cog):

    def _init_(self,client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Webscrape loaded!')

    #commands
    @commands.command()

    async def elevators(self,ctx):

        page = requests.get("https://uofaescalator.com/")

        
        soup = BeautifulSoup(page.content, 'html.parser')
        

        element = soup.find('div', {"style": "font-size:10em;color:green;"})

        eStatus = element.text

        if eStatus == "Yes.":
            await ctx.send("Yay! LRT Escalators are working")
        else:
            await ctx.send("Sorry! LRT Escalators are not working")

    @commands.command()
    async def greeting(self,ctx):
        
        await ctx.send('Hello')





def setup(client):
        client.add_cog(webCommands(client))


    





