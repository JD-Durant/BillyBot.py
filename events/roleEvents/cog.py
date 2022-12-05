from discord.ext import commands
import datetime
import discord

class roleEvents(commands.Cog):
    """IGNORE | Bot Listeners"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        logChannel = None
        possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
        for iterateChannel in role.guild.channels:
            for i in possibleLogChannels:
                if i in iterateChannel.name:
                    logChannel = discord.utils.get(role.guild.text_channels, name=iterateChannel.name)
        if logChannel:
            discordEmbed=discord.Embed(title="🏅 Role Created : {}".format(role.name), description="", color=0x00fc8a)
            discordEmbed.set_author(name=role.guild.name, icon_url=role.guild.icon_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_footer(text="Role ID : {}".format(role.id))
            await logChannel.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
            discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
            await discord.utils.get(role.guild.text_channels, name="general").send(embed=discordEmbed)
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        logChannel = None
        possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
        for iterateChannel in role.guild.channels:
            for i in possibleLogChannels:
                if i in iterateChannel.name:
                    logChannel = discord.utils.get(role.guild.text_channels, name=iterateChannel.name)
        if logChannel:
            discordEmbed=discord.Embed(title="🏅 Role Deleted : {}".format(role.name), description="", color=0x8D021F)
            discordEmbed.set_author(name=role.guild.name, icon_url=role.guild.icon_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_footer(text="Role ID : {}".format(role.id))
            await logChannel.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
            discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
            await discord.utils.get(role.guild.text_channels, name="general").send(embed=discordEmbed)
    
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        logChannel = None
        possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
        for iterateChannel in before.guild.channels:
            for i in possibleLogChannels:
                if i in iterateChannel.name:
                    logChannel = discord.utils.get(before.guild.text_channels, name=iterateChannel.name)
        if logChannel:
            if before.name != after.name:
                discordEmbed=discord.Embed(title="🏅 Role Edited", description="", color=0xffbf00)
                discordEmbed.add_field(name='🏷️Name Changed : `{}` -> `{}`'.format(before.name, after.name), value="** **", inline=False)
            elif before.color != after.color:
                discordEmbed=discord.Embed(title="🏅 Role Edited", description="", color=0xffbf00)
                discordEmbed.add_field(name='🎨Colour Changed : `{}` -> `{}`'.format(before.color, after.color), value="** **", inline=False)
            else:
                return
            discordEmbed.set_author(name=before.guild.name, icon_url=before.guild.icon_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_footer(text="Role ID : {}".format(after.id))
            await logChannel.send(embed=discordEmbed)
        else:
            discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
            discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
            await discord.utils.get(before.guild.text_channels, name="general").send(embed=discordEmbed)
            
def setup(bot):
    bot.add_cog(roleEvents(bot))