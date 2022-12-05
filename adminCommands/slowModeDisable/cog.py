from discord.ext import commands
import discord
import datetime
import asyncio

class slowmodedisable(commands.Cog, name="slowModeDisable"):
    """A | Turns off slow mode"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['slowmodeoff'])
    @commands.has_permissions(administrator=True)
    async def slowmodedisable(self, ctx: commands.Context):
        """?slowmodeoff"""
        await ctx.channel.edit(slowmode_delay=0)
        embed = discord.Embed(title="Slow mode disabled",description=f"Slowmode disabled by {ctx.author.mention} 🔒",color=0x00fc8a)
        embed.add_field(name="Channel affected", value=ctx.channel, inline=True)
        embed.add_field(name=":warning: | Important", value="**Users with Administrator perms won't be affected**", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.channel.send(embed=embed)

        
def setup(bot: commands.Bot):
    bot.add_cog(slowmodedisable(bot))