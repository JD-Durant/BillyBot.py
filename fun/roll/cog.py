from discord.ext import commands
import time
import random

class roll(commands.Cog, name="roll"):
    """F | Rolls a dice"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['d', 'dice'])
    async def roll(self, ctx: commands.Context, *arg):
        """?roll {Optional : dicesize}(default : 6)"""
        if not arg:
            rollMessage = await ctx.send("Rolling 🎲")
            time.sleep(1)
            await rollMessage.edit(content="{} Rolled a {} 🎲".format(ctx.author.mention, random.randint(1, 6)))
        else:
            try:
                argInt = int(arg[0])
            except ValueError as verr:
                await ctx.send("**Please enter a number!**")
                return
            if argInt <= 0:
                await ctx.send("**Please enter a number above 0!**")
                return
            rollMessage = await ctx.send("Rolling 🎲")
            time.sleep(1)
            await rollMessage.edit(content="{} Rolled a {} 🎲".format(ctx.author.mention, random.randint(1, argInt)))
        

def setup(bot: commands.Bot):
    bot.add_cog(roll(bot))