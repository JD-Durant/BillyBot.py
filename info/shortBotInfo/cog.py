from discord.ext import commands
import time
import discord
import random
import botmain
import datetime

class shortBotInfo(commands.Cog, name="shortBotInfo"):
    """I | Shows Shorter Bot Info"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['activity', 'shortinfo'])
    async def shortBotInfo(self, ctx: commands.Context):
        """?shortBotInfo"""
        memberCount = 0
        guildCount = 0
        amIListening = "I am not currently listening to anything!"
        for guild in self.bot.guilds:
            memberCount=memberCount + len(guild.members)
            guildCount=guildCount + 1
        if botmain.currentVoiceGuild is not None:
            amIListening = "Listening to music in a server!"
        discordEmbed = discord.Embed(title="Billy's Info", description="", color=0x00fc8a)
        discordEmbed.add_field(name='⏰ Uptime', value=f"{str(datetime.timedelta(seconds=int(round(time.time()-botmain.startTime))))}", inline=True)
        discordEmbed.add_field(name='🎵 Currently Playing?', value = f'{amIListening}', inline = True)
        discordEmbed.set_footer(text=f"Billy is running {botmain.version}")
        discordEmbed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=discordEmbed)

def setup(bot: commands.Bot):
    bot.add_cog(shortBotInfo(bot))