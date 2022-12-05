from discord.ext import commands
import discord
import botmain

class leave(commands.Cog, name="leave"):
    """M | Leaves current vc"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def leave(self, ctx: commands.Context):
        """?leave"""
        if discord.utils.get(ctx.guild.roles, name="Muted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if botmain.currentVoiceGuild is not None:
            if botmain.currentVoiceGuild != ctx.guild:
                await ctx.send("Sorry! I am currently playing in another server!")
                return
        if voice.is_connected():
            await voice.disconnect()
            botmain.song_queue.clear()
            botmain.currentVoiceGuild = None
            await ctx.message.add_reaction('👋')
        else:
            await ctx.send("**I'm not connected to a voice channel!**")


def setup(bot: commands.Bot):
    bot.add_cog(leave(bot))

    