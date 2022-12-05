from discord.ext import commands
import discord
import botmain
import asyncio

class voiceEvents(commands.Cog):
    """IGNORE | Bot Listeners"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.id != self.client.user.id:
            return
        if before.channel is None:
            possibleCommandChannels = ['music-commands', 'bot-commands', 'bot︲commands']
            voice = after.channel.guild.voice_client
            timeInactive = 0
            while True:
                musicChannel = None
                await asyncio.sleep(1)
                timeInactive = timeInactive + 1
                if voice.is_playing() and not voice.is_paused():
                    timeInactive = 0
                if timeInactive == 180:
                    await voice.disconnect()
                    botmain.currentVoiceGuild = None
                    for channel in member.guild.channels:
                        for i in possibleCommandChannels:
                            if i in channel.name:
                                musicChannel = discord.utils.get(after.channel.guild.text_channels, name=channel.name)
                    if musicChannel:
                        botmain.song_queue.clear()
                        await musicChannel.send("**Disconnected due to lack of activity** 👋")
                    else:
                        botmain.song_queue.clear()
                        discordEmbed = discord.Embed(title=":warning: Warning :warning:", description="", color=0x8D021F)
                        discordEmbed.add_field(name='**There is no command channel setup for me!**\n **Please make one with one of the following names!**', value='\n`music-commands`\n  `bot-commands`\n  `bot︲commands`', inline=False)
                        await discord.utils.get(after.channel.guild.text_channels, name="general").send(embed=discordEmbed)
                if not voice.is_connected():
                    break
        elif after.channel is None:
            self.client.currentVoiceGuild = None
            
def setup(bot):
    bot.add_cog(voiceEvents(bot))