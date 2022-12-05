from discord.ext import commands
import discord
import datetime
from discord.ext.commands import cooldown, BucketType
import random
import asyncio
class rps(commands.Cog, name="rps"):
    """F | Rock paper scissors!"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def create_embed(self, ctx, status, outCome, outComeText):
        discordEmbed = discord.Embed(title="{}".format(status),description="{} vs {}".format(ctx.author.mention, '<@940105098942627860>'), color=0x00fc8a)
        discordEmbed.add_field(name="{}".format(outCome), value="{}".format(outComeText), inline=True)
        discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        discordEmbed.timestamp = datetime.datetime.utcnow()
        return discordEmbed

    @commands.cooldown(1, 8, commands.BucketType.user)
    @commands.command(alises=['rockpaperscissors'])
    async def rps(self, ctx: commands.Context):
        """?rps"""
        gameEmojis = ['🧱', '🧻', '✂️']
        for emoji in gameEmojis:
            await ctx.message.add_reaction(emoji)
        timerEmojis = ['🕛', '🕒', '🕕' ,'🕘', '🕛', '🔫']
        for emoji in timerEmojis:
            await ctx.message.add_reaction(emoji)
            await asyncio.sleep(1)
            await ctx.message.clear_reaction(emoji)
        users = set()
        for reaction in ctx.message.reactions:
            async for user in reaction.users():
                users.add(user)
        userReactedTo = None
        if any(reaction.emoji in gameEmojis for reaction in ctx.message.reactions):
            for i in ctx.message.reactions:
                if i.count >= 2:
                    for user in users:
                        if ctx.author.id == user.id:
                            if userReactedTo is None:
                                userReactedTo = str(i)
                            else:
                                await ctx.send(embed=self.create_embed(ctx, "Disqualified", "Reason", "Too many choices! 👎"))
                                await ctx.message.clear_reactions()
                                await ctx.message.add_reaction('👎')
                                return
        if userReactedTo is None:
            await ctx.send(embed=self.create_embed(ctx, "Billy Wins!", "Reason", "Opponent didn't choose anything!"))
            await ctx.message.clear_reactions()
            await ctx.message.add_reaction('👎')
            return
        botWin = None
        rareEvent = random.randrange(1, 1001)
        if rareEvent == 1000:
            botChoice = '🔫'
            botWin = True
        else:
            botChoice = random.choice(gameEmojis)
        if userReactedTo == botChoice:
            await ctx.send(embed=self.create_embed(ctx, "Tie! GG!", "Results", "You Chose : {} | Billy chose : {}".format(userReactedTo, botChoice)))
            #await ctx.send("{} | Tie! GG! You Chose : {} | Billy chose : {}".format(ctx.author.mention, userReactedTo, botChoice))
            await ctx.message.clear_reactions()
            return
        elif "🧱" in userReactedTo:
            if '🧻' in botChoice:
                botWin = True
        elif "🧻" in userReactedTo:
            if '✂️' in botChoice:
                botWin = True
        elif "✂️" in userReactedTo:
            if '🧱' in botChoice:
                botWin = True
        else:
            await ctx.send(embed=self.create_embed(ctx, "Disqualified", "Reason", "Non Tournament Regulated Approved Emoji used! 👎"))
            await ctx.message.clear_reactions()
            return
        await ctx.message.clear_reactions()
        if botWin == True:
            await ctx.send(embed=self.create_embed(ctx, "Billy Wins!", "Results", "You Chose : {} | Billy chose : {}".format(userReactedTo , botChoice)))
            #await ctx.send("{} | You lose! GG! You Chose: {} | Billy chose : {}".format(ctx.author.mention, userReactedTo, botChoice))
        else:
            await ctx.send(embed=self.create_embed(ctx, "👑 You Win! 👑".format(ctx.author.mention), "Results", "You Chose : {} | Billy chose : {}".format(userReactedTo , botChoice)))
            #await ctx.send("{} | You win! GG! You Chose: {} | Billy chose : {}".format(ctx.author.mention, userReactedTo, botChoice))
            await ctx.message.add_reaction('🏆')

def setup(bot: commands.Bot):
    bot.add_cog(rps(bot))