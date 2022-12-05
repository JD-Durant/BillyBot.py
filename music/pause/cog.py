import asyncio
from discord.ext import commands
import discord
from discord.utils import get

class pause(commands.Cog, name="pause"):
    """M | Pauses music"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def pause(self, ctx: commands.Context):
        """?pause"""
        if discord.utils.get(ctx.guild.roles, name="Muted") in ctx.author.roles:
            await ctx.send("You are currently blacklisted!")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice:
            await ctx.send("**Not connected to a VC in this server!**")
            return
        if voice.is_playing():
            voice.pause()
            pauseMessage = await ctx.send("**Music has been paused!**")
            resume = False
            resumeEmoji = '⏯️'
            await ctx.message.add_reaction(resumeEmoji)
            timerEmojis = ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚' ,'🕛']
            for emoji in timerEmojis:
                await ctx.message.add_reaction(emoji)
                await asyncio.sleep(2)
                await ctx.message.clear_reaction(emoji)
                if any(reaction.emoji == resumeEmoji for reaction in ctx.message.reactions):
                    for i in ctx.message.reactions:
                        if i.count == 2:
                            await pauseMessage.delete()
                            voice.resume()
                            resume = True
                            await ctx.send("**Music has been resumed!**")
                if resume == True:
                    break
            await ctx.message.clear_reaction(resumeEmoji)
        else:
            await ctx.send("**No audio is playing!**")

def setup(bot: commands.Bot):
    bot.add_cog(pause(bot))