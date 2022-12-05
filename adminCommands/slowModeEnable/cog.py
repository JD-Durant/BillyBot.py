from discord.ext import commands
import discord
import datetime
import asyncio

class slowmodeenable(commands.Cog, name="slowModeEnable"):
    """A | Sets channel to slow mode"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['slowmode', 'slowmodeon'])
    @commands.has_permissions(administrator=True)
    async def slowmodeenable(self, ctx: commands.Context, seconds:int=None):
        """?slowmode {Optional : seconds(default is 10)}"""
        if seconds is None:
            seconds = 10
            await ctx.channel.edit(slowmode_delay=10)
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(title="Slow mode enabled",description=f"Slowmode enabled by {ctx.author.mention} 🔒",color=0x00fc8a)
        embed.add_field(name="Delay", value=seconds, inline=True)
        embed.add_field(name="Channel affected", value=ctx.channel, inline=True)
        embed.add_field(name=":warning: | Important", value="**Users with Administrator perms won't be affected**", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.channel.send(embed=embed)

        
def setup(bot: commands.Bot):
    bot.add_cog(slowmodeenable(bot))