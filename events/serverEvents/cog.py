from discord.ext import commands
import datetime
import discord

class serverEvents(commands.Cog):
    """IGNORE | Bot Listeners"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        logChannel = None
        possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
        for iterateChannel in channel.guild.channels:
            for i in possibleLogChannels:
                if i in iterateChannel.name:
                    logChannel = discord.utils.get(channel.guild.text_channels, name=iterateChannel.name)
        if logChannel:
            if type(channel) == discord.TextChannel:
                discordEmbed=discord.Embed(title="📝 Text Channel Created : #{}".format(channel.name), description="", color=0x00fc8a)
            else:
                discordEmbed=discord.Embed(title="📣 Voice Channel Created : #{}".format(channel.name), description="", color=0x00fc8a)
            discordEmbed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_footer(text="Channel ID : {}".format(channel.id))
            await logChannel.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
            discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
            await discord.utils.get(channel.guild.text_channels, name="general").send(embed=discordEmbed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        logChannel = None
        possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
        for iterateChannel in channel.guild.channels:
            for i in possibleLogChannels:
                if i in iterateChannel.name:
                    logChannel = discord.utils.get(iterateChannel.guild.text_channels, name=iterateChannel.name)
        if logChannel:
            if type(channel) == discord.TextChannel:
                discordEmbed=discord.Embed(title="📝 Text Channel Deleted : #{}".format(channel.name), description="", color=0x8D021F)
                discordEmbed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
                discordEmbed.set_footer(text="Channel ID : {}".format(channel.id))
                discordEmbed.timestamp = datetime.datetime.utcnow()
                await logChannel.send(embed=discordEmbed)
            else:
                discordEmbed=discord.Embed(title="📣 Voice Channel Deleted : #{}".format(channel.name), description="", color=0x8D021F)
                discordEmbed.set_author(name=channel.guild.name, icon_url=channel.guild.icon_url)
                discordEmbed.timestamp = datetime.datetime.utcnow()
                discordEmbed.set_footer(text="Channel ID : {}".format(channel.id))
                await logChannel.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
            discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
            await discord.utils.get(channel.guild.text_channels, name="general").send(embed=discordEmbed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        logChannel = None
        possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
        for iterateChannel in before.guild.channels:
            for i in possibleLogChannels:
                if i in iterateChannel.name:
                    logChannel = discord.utils.get(before.guild.text_channels, name=iterateChannel.name)
        if logChannel:
            if before.name != after.name:
                if type(before) == discord.TextChannel:
                    discordEmbed=discord.Embed(title="📝 Text Channel Edited".format(before.name), description="", color=0xffbf00)
                else:
                    discordEmbed=discord.Embed(title="📣 Voice Channel Edited".format(before.name), description="", color=0xffbf00)
            else:
                return
            discordEmbed.add_field(name='🏷️Name Changed : `#{}` -> `#{}`'.format(before.name, after.name), value="** **", inline=False)
            discordEmbed.set_author(name=before.guild.name, icon_url=before.guild.icon_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_footer(text="Role ID : {}".format(after.id))
            await logChannel.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
            discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
            await discord.utils.get(before.guild.text_channels, name="general").send(embed=discordEmbed)


            
def setup(bot):
    bot.add_cog(serverEvents(bot))