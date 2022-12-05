from discord.ext import commands
import asyncio

class Purge(commands.Cog, name="purge"):
    """A | Clears messages in selected channel"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['clear'])
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx: commands.Context, amount=5):
        """?clear {Optional : amount(default is 5)}"""
        amount = amount + 1
        await ctx.channel.purge(limit=amount)
        clearMessage = await ctx.send("Done! deleted `{} messages` {}".format(amount-1, ctx.author.mention))
        await asyncio.sleep(3)
        await clearMessage.delete()

        
def setup(bot: commands.Bot):
    bot.add_cog(Purge(bot))