from discord.ext import commands
import time
import discord
import random
import botmain
import datetime

class serverInfo(commands.Cog, name="serverInfo"):
    """I | Shows Server Info"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def serverInfo(self, ctx: commands.Context):
        """?serverInfo"""
        textChannelAmounts = 0
        voiceChannelAmounts = 0
        memberCount = 0
        botCount = 0
        for channel in ctx.guild.channels:
            if str(channel.type) == 'text':
                textChannelAmounts = textChannelAmounts + 1
            elif str(channel.type) == 'voice':
                voiceChannelAmounts = voiceChannelAmounts + 1
        for i in ctx.guild.member:
            if not i.bot:
                memberCount+=1
            else:
                botCount+=1
        discordEmbed = discord.Embed(title = f"{ctx.guild.name} Info", description = "", color=0x00fc8a)
        discordEmbed.add_field(name = '🆔Server ID', value = f"{ctx.guild.id}", inline = True)
        discordEmbed.add_field(name = '📆Created On', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
        discordEmbed.add_field(name = '👑Owner', value = f"{ctx.guild.owner}", inline = True)
        discordEmbed.add_field(name = '👥Members', value = f'{memberCount} Members', inline = True)
        discordEmbed.add_field(name = '🤖Bots', value = f'{botCount} Bots', inline = True)
        discordEmbed.add_field(name = '💬 Text Channels', value = f'{textChannelAmounts}', inline = True)
        discordEmbed.add_field(name = '🔊 Voice Channels', value = f'{voiceChannelAmounts}', inline = True)
        discordEmbed.set_thumbnail(url = ctx.guild.icon_url)
        discordEmbed.set_footer(text=f"Billy is running {botmain.version}")
        await ctx.send(embed=discordEmbed)


def setup(bot: commands.Bot):
    bot.add_cog(serverInfo(bot))