from discord.ext import commands
import time
import random
eightballList = []
eightballList = [line.strip() for line in open("Text Files/8Ball.txt", 'r')]

class eightBall(commands.Cog, name="8Ball"):
    """F | Predicts the future"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=["8ball"])
    async def eightBall(self, ctx: commands.Context):
        """?8ball {question}"""
        thinkingMessage = await ctx.send("Thinking :thinking:")
        time.sleep(1)
        await thinkingMessage.edit(content= "{}, {}".format(random.choice(eightballList), ctx.author.mention))

def setup(bot: commands.Bot):
    bot.add_cog(eightBall(bot))