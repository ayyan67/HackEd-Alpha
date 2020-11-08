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

        def print_cards(hand):
            card_list = list(map(str, hand))
            return (",".join(card_list))

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
        
        print("Player Cards:", player_cards)    # debug
        print("Dealer Cards:", dealer_cards)    # debug

        player_total = eval_hand(player_cards)
        dealer_total = eval_hand(dealer_cards)

        intial_hand = True
        flag = False
  
        # display blackjack header
        await ctx.send("You are playing Blackjack...")

        # initial_hand  
        if intial_hand:
            await ctx.send("Your cards are: [{}], Total is: {}".format(print_cards(player_cards), eval_hand(player_cards)))
            await ctx.send("Dealer has: [{}][?]".format(dealer_cards[0]))

        # initial_hand player win or push
        if (intial_hand) and (player_total == 21) and (dealer_total != 21):
            await ctx.send("BLACKJACK! You Win!")
            await ctx.send("Dealer had: [{}], Total was: {}".format(print_cards(dealer_cards), eval_hand(dealer_cards)))
            flag = True
        elif (player_total == dealer_total == 21):
            await ctx.send("Push, nobody wins")
            flag = True
       
       #    
        stand = False        
        while flag == False: 

            # busted and win scenarios
            if (eval_hand(player_cards) > 21) and (eval_hand(dealer_cards) <= 21):
                await ctx.send("You are busted! Dealer Wins!")
                break
            elif (eval_hand(dealer_cards) > 21) and (eval_hand(player_cards) <= 21):
                await ctx.send("Dealer is busted, You Win!")
                break
            
            # stand scenarios
            # player chooses to stand as their cards total is <= 21
            if stand:
                if eval_hand(dealer_cards) > 21:
                    await ctx.send("Dealer is busted, You Win!")
                    break 
                elif eval_hand(player_cards) == eval_hand(dealer_cards):
                    await ctx.send("Push, nobody wins")
                elif eval_hand(player_cards) > eval_hand(dealer_cards):
                    await ctx.send("Your cards total is higher than the dealer. You Win!")
                    break
                else:
                    await ctx.send("Your cards total is lower than the dealer. You Lose!")
                    break
        
            await ctx.send(f"Please type '!h' to hit or '!s' to stay")
            message = await self.client.wait_for("message")    
            if message.content == ("!h"):
                player_cards.append(cards.pop())
            elif (message.content == ("!s")) or (message.content == ("")):
                stand = True
                
                # dealer must hit until their card total is greater than 16
                while eval_hand(dealer_cards) <= 16:
                    dealer_cards.append(cards.pop())

            # print blackjack state        
            await ctx.send("You are playing Blackjack...")
            await ctx.send("Your cards are: [{}], Total is: {}".format(print_cards(player_cards), eval_hand(player_cards)))
            await ctx.send("Dealer has: [{}], Total is: {}".format(print_cards(dealer_cards), eval_hand(dealer_cards)))

def setup(client):
    client.add_cog(CardGame(client))