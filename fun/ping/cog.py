from discord.ext import commands
import asyncio
import botmain
import datetime, time

class Ping(commands.Cog, name="Ping"):
    """F | Checks the latency"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def ping(self, ctx: commands.Context):
        """?ping"""
        await ctx.send(f"{ctx.author.mention} Pong! in {round(self.bot.latency * 1000)}ms")

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))