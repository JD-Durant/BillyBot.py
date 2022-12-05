from discord.ext import commands
import botmain
import datetime, time

class uptime(commands.Cog, name="upTime"):
    """Checks the uptime"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def uptime(self, ctx: commands.Context):
        """?uptime"""
        currentTime = time.time()
        difference = int(round(currentTime - botmain.startTime))
        text = str(datetime.timedelta(seconds=difference))
        await ctx.send("I have been online for {}s".format(str(datetime.timedelta(seconds=int(round(time.time()-botmain.startTime))))))

def setup(bot: commands.Bot):
    bot.add_cog(uptime(bot))