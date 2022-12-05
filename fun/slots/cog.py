from discord.ext import commands
import botmain
import datetime, time
import random
import discord

class slots(commands.Cog, name="slots"):
    """F | Slot machine"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def slots(self, ctx: commands.Context, coins:int=None):
        """?slots {optional : coins(default is 10)"""
        if coins is None:
            coins = 10
        if coins > 10000:
            await ctx.send("Keep your bets below 10k!")
            return
        if coins < 1:
            await ctx.send("You can't bet less than 1 coin!")
            return
        topRow = []
        outCome = []
        bottomRow = []
        for i in range(3):
            outcome = random.choice([":coin:", ":money_with_wings:", ":seven:"])
            outCome.append(outcome)
        for i in range(3):
            toprow = random.choice(["🍊", "🍋", "💎"])
            topRow.append(toprow)
        for i in range(3):
            bottomrow = random.choice(["🍒", "🍉", "🔔"])
            bottomRow.append(bottomrow)
        if outCome[0]==outCome[1]==outCome[2]:
            discordEmbed = discord.Embed(title="You win!",description="", color=0x00fc8a)
            discordEmbed.add_field(name="  ".join(topRow), value="** **", inline=False)
            discordEmbed.add_field(name="{}           ===WINNING ROW".format("  ".join(outCome)), value="** **", inline=False)
            discordEmbed.add_field(name="  ".join(bottomRow), value="Bet placed : {} :coin: | Amount won : {} 💰".format(coins, coins*20), inline=False)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title="You lose!",description="", color=0x00fc8a)
            discordEmbed.add_field(name="  ".join(topRow), value="** **", inline=False)
            discordEmbed.add_field(name="{}           ===WINNING ROW".format("  ".join(outCome)), value="** **", inline=False)
            discordEmbed.add_field(name="  ".join(bottomRow), value="Bet placed : {} :coin:".format(coins), inline=False)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=discordEmbed)



def setup(bot: commands.Bot):
    bot.add_cog(slots(bot))