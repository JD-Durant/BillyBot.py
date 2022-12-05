from discord.ext import commands
import datetime
import discord
import random
easterEggs = ['thanks billy', 'thank you billy', 'ty billy', 'tyvm billy', 'thank you, billy']
easterEggs2 = ['love u billy', 'love you billy', 'luv u billy', 'luv you billy', 'i love u billy', 'i luv u billy', 'i love you billy', 'i love u billy', 'love you, billy']
easterEggs3 = ['fuck u billy', 'fuck off billy', 'fuck you billy', 'fuck billy']

class messageEvents(commands.Cog):
    """IGNORE | Bot Listeners"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.id == self.client.user.id:
            return
        else:
            logChannel = None
            possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
            for channel in message.author.guild.channels:
                for i in possibleLogChannels:
                    if i in channel.name:
                        logChannel = discord.utils.get(message.channel.guild.text_channels, name=channel.name)
            if logChannel:
                discordEmbed = discord.Embed(title="Message sent by @{} has been deleted in #{}".format(message.author, message.channel), description=f"{message.content}", color=0x8D021F)
                discordEmbed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                discordEmbed.set_footer(text="Message ID : {} | Author ID : {}".format(message.id, message.author.id))
                discordEmbed.timestamp = datetime.datetime.utcnow()
                await logChannel.send(embed=discordEmbed)
            else:
                discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
                discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
                discordEmbed.timestamp = datetime.datetime.utcnow()
                await discord.utils.get(message.channel.guild.text_channels, name="general").send(embed=discordEmbed)

        
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.id == self.client.user.id:
            return
        if before.content == after.content:
            return
        else:
            logChannel = None
            possibleLogChannels = ['bot-log', 'bot︲log', 'bot-logs', 'bot︲logs']
            for channel in after.guild.channels:
                for i in possibleLogChannels:
                    if i in channel.name:
                        logChannel = discord.utils.get(after.channel.guild.text_channels, name=channel.name)
            if logChannel:
                discordEmbed=discord.Embed(title="Message Edited by @{} in #{}".format(before.author, before.channel), description="", color=0xffbf00)
                discordEmbed.add_field(name="Old Message",value="{}".format(before.content), inline=False)
                discordEmbed.add_field(name="New Message",value="{}".format(after.content), inline=False)
                discordEmbed.set_author(name=before.author.name, icon_url=before.author.avatar_url)
                discordEmbed.set_footer(text="Message ID : {} | Author ID : {}".format(before.id, before.author.id))
                discordEmbed.timestamp = datetime.datetime.utcnow()
                await logChannel.send(embed=discordEmbed)
            else:
                discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
                discordEmbed.add_field(name='**There is no log channel setup for me!**\n **Please make one with one of the following names!**', value='\n`bot-log`\n  `bot︲log`\n  `bot-logs`\n `bot︲logs`', inline=False)
                await discord.utils.get(before.channel.guild.text_channels, name="general").send(embed=discordEmbed)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content.lower()
        splitMessage = list(msg)
        if splitMessage:
            if "is billy sentient" in msg:
                await message.reply("Yes. definetly.")
            elif "easter egg" in msg:
                rareEvent = random.randrange(1, 4)
                if rareEvent == 3:
                    await message.author.send("❗❗❗ **You found an Easter Egg!** ❗❗❗\n**But keep this between us** 😉\n\n ⬇️To claim follow the instructions in the below video!⬇️\nhttps://streamable.com/zsnx5v")
            elif "billy @everyone" in msg:
                await message.reply("@everyone")
            elif msg in easterEggs:
                await message.reply("You're welcome :D")
            elif msg in easterEggs2:
                await message.reply("Love you 2 <3")
            elif msg in easterEggs3:
                await message.reply("Cope harder :skull:")
            
def setup(bot):
    bot.add_cog(messageEvents(bot))