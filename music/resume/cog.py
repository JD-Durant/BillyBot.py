import asyncio
from discord.ext import commands
import discord
from discord.utils import get

class resume(commands.Cog, name="resume"):
    """M | Continues playing music"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def resume(self, ctx: commands.Context):
        """?resume"""
        if discord.utils.get(ctx.guild.roles, name="Muted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice:
            await ctx.send("**Not connected to a VC in this server!**")
            return
        if voice.is_paused():
            voice.resume()
            resumeMessage = await ctx.send("**Music has been resumed!**")
            pauseBool = False
            pauseEmoji = '⏯️'
            await ctx.message.add_reaction(pauseEmoji)
            timerEmojis = ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚' ,'🕛']
            for emoji in timerEmojis:
                await ctx.message.add_reaction(emoji)
                await asyncio.sleep(2)
                await ctx.message.clear_reaction(emoji)
                if any(reaction.emoji == pauseEmoji  for reaction in ctx.message.reactions):
                    for i in ctx.message.reactions:
                        if i.count == 2:
                            await resumeMessage.delete()
                            voice.pause()
                            pauseBool = True
                            await ctx.send("**Music has been paused!**")
                if pauseBool == True:
                    break
            await ctx.message.clear_reaction(pauseEmoji)
        else:
            await ctx.send("**No audio is playing!**")

def setup(bot: commands.Bot):
    bot.add_cog(resume(bot))