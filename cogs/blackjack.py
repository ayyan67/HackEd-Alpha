import discord
from discord.ext import commands
import random
import asyncio

class CardGame(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Card Game Loaded")

    @commands.command()
    async def blackjack(self,ctx):

        def eval_hand(hand):

            non_aces = [card for card in hand if card != 'A']
            aces = [card for card in hand if card == 'A']

            total = 0

            for card in non_aces:
                if card in ['J','Q','K']:
                    total += 10
                else:
                    total += int(card)
            
            for card in aces:
                if total <= 10:
                    total += 11
                else:
                    total += 1

            return total

        cards = [
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
            '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        ]

        random.shuffle(cards)

        player_cards = []
        dealer_cards = []

        player_cards.append(cards.pop())
        dealer_cards.append(cards.pop())
        player_cards.append(cards.pop())
        dealer_cards.append(cards.pop())

        player_total = eval_hand(player_cards)
        dealer_total = eval_hand(dealer_cards)

        await ctx.send("Your cards are " + print(*player_cards, sep=',') +
        ", Total Score: " + player_total + "\nDealer has " + print(*dealer_cards, sep=','))
    

def setup(client):
    client.add_cog(CardGame(client))