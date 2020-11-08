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

#8ball Game
    
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

#Card Game

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

        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4

        random.shuffle(cards)

        player_cards = []
        dealer_cards = []

        player_cards.append(cards.pop())
        dealer_cards.append(cards.pop())
        player_cards.append(cards.pop())
        dealer_cards.append(cards.pop())
        
        # print("Player Cards:", player_cards)    # to see player cards in the terminal
        # print("Dealer Cards:", dealer_cards)    # to see dealer cards in the terminal

        player_total = eval_hand(player_cards)
        dealer_total = eval_hand(dealer_cards)

        intial_hand = True
        flag = False

        # display blackjack header
        await ctx.send("You are playing Blackjack...")

        # deal the cards 
        if intial_hand:
            await ctx.send("Your cards are: [{}], Total is: {}".format(print_cards(player_cards), eval_hand(player_cards)))
            await ctx.send("Dealer's cards are: [{}][?]".format(dealer_cards[0]))

        # player win or push scenarios with initial-hand
        if (intial_hand) and (player_total == 21) and (dealer_total != 21):
            await ctx.send("BLACKJACK! You Win!")
            await ctx.send("Dealer's cards were: [{}], Total was: {}".format(print_cards(dealer_cards), eval_hand(dealer_cards)))
            flag = True
        elif (player_total == dealer_total == 21):
            await ctx.send("Push, nobody wins")
            flag = True
    
        # after initial-hand scenarios
        stay = False        
        while flag == False: 

            # busted and win scenarios
            if (eval_hand(player_cards) > 21) and (eval_hand(dealer_cards) <= 21):
                await ctx.send("You are busted! Dealer Wins!")
                break
            elif (eval_hand(dealer_cards) > 21) and (eval_hand(player_cards) <= 21):
                await ctx.send("Dealer is busted, You Win!")
                break
            
            # stay scenarios
            # player chooses to stay as their cards total is <= 21
            if stay:
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
        
            # player is forced to stay if they do not type '!h' or '!s'
            await ctx.send(f"Please type '!h' to hit or '!s' to stay")
            message = await self.client.wait_for("message")    
            if message.content == ("!h"):
                player_cards.append(cards.pop())
            elif (message.content == ("!s")) or (message.content == ("")):
                stay = True
                
                # dealer must hit until their card total is greater than 16
                while eval_hand(dealer_cards) <= 16:
                    dealer_cards.append(cards.pop())

            # print blackjack state
            # only reveal the dealer's hand once the player chooses to stay
            await ctx.send("You are playing Blackjack...")
            await ctx.send("Your cards are: [{}], Total is: {}".format(print_cards(player_cards), eval_hand(player_cards)))
            if stay == False:        
                await ctx.send("Dealer's cards are: [{}][?]".format(dealer_cards[0]))
            else:
                await ctx.send("Dealer's cards are: [{}], Total is: {}".format(print_cards(dealer_cards), eval_hand(dealer_cards)))

    ###########

def setup(client):
    client.add_cog(Games(client))
