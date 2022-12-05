from discord.ext import commands
import time
import discord
import random
import botmain
import datetime

class botInfo(commands.Cog, name="botInfo"):
    """I | Shows Bot Info"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def botInfo(self, ctx: commands.Context):
        """?botinfo"""
        memberCount = 0
        guildCount = 0
        amIListening = "I am not currently listening to anything!"
        for guild in self.bot.guilds:
            memberCount=memberCount + len(guild.members)
            guildCount=guildCount + 1
        if botmain.currentVoiceGuild is not None:
            amIListening = "Listening to music in a server!"
        discordEmbed = discord.Embed(title="Billy's Info", description=f"Current Ping : {round(self.bot.latency * 1000)}ms", color=0x00fc8a)
        discordEmbed.add_field(name='👑 Owner', value="Jösh#6546", inline=True)
        discordEmbed.add_field(name='📆 Created On', value = "February 7th 2022", inline = True)
        discordEmbed.add_field(name='💻 Github', value = "[Click Me!](https://github.com/JD-Durant)", inline = True)
        discordEmbed.add_field(name='📝 Info', value="```\nBillyBotJr is the successor to Billy Bot! He can do many things his father could once do, but much better!\n\nThis bot is developed by Jösh#6546, utilising the discord.py library. If you have any questions or suggestions, feel free to message me\n```", inline=False)
        discordEmbed.add_field(name='⏰ Uptime', value=f"{str(datetime.timedelta(seconds=int(round(time.time()-botmain.startTime))))}", inline=True)
        discordEmbed.add_field(name='🌎 Region', value = 'Europe', inline = True)
        discordEmbed.add_field(name='👥 Total Users', value = f'{memberCount} Users', inline = True)
        discordEmbed.add_field(name='💬 Total Servers', value = f'{guildCount} Servers', inline = True)
        discordEmbed.add_field(name='🎵 Currently Playing?', value = f'{amIListening}', inline = True)
        discordEmbed.add_field(name='⭐ Prefix', value = '? (Do ?help to see all commands!)', inline = True)
        discordEmbed.set_footer(text=f"Billy is running {botmain.version}")
        discordEmbed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=discordEmbed)

def setup(bot: commands.Bot):
    bot.add_cog(botInfo(bot))