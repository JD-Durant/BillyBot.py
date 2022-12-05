from discord.ext import commands
import discord
from discord.utils import get
import botmain
import asyncio

class remove(commands.Cog, name="remove"):
    """M | Removes song or clears queue"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['cq', 'r'])
    async def remove(self, ctx: commands.Context, arg:int=None):
        """?remove {Optional : song position}"""
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        queueLength = len(botmain.song_queue)
        if discord.utils.get(ctx.guild.roles, name="Groove Master") in ctx.author.roles:
            if arg is not None:
                if arg > queueLength:
                    await ctx.send("**There are only {} songs in the queue!**".format(len(botmain.song_queue)))
                elif arg == 1:
                    arg = arg - 1
                    await ctx.send("**{}** has been removed from the queue".format(botmain.song_queue[arg]['title']))
                    voice.stop()
                else:
                    arg = arg - 1
                    await ctx.send("**{}** has been removed from the queue".format(botmain.song_queue[arg]['title']))
                    del botmain.song_queue[arg]
            else:
                botmain.song_queue.clear()
                voice.stop()
                await ctx.send("**Queue has been cleared and music has been stopped!**")
        else:
            if voice.is_connected():
                if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
                    vcChannel = ctx.message.author.voice.channel
                    x = 0
                    if arg > len(botmain.song_queue):
                        await ctx.send("**There are only {} songs in the queue!**".format(len(botmain.song_queue)))
                        return
                    elif arg == 1:
                        await ctx.send("**Please use ?skip or ?stop instead!**")
                    else:
                        for i in vcChannel.members:
                            x = x + 1
                        if x >=3:
                            arg = arg - 1
                            songImageUrl = botmain.song_queue[arg]['url']
                            reaction = '\N{THUMBS UP SIGN}'
                            discordEmbed = discord.Embed(title="Remove Vote", description="", color=0x00fc8a)
                            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                            discordEmbed.add_field(name="Current Song", value="{}".format(botmain.song_queue[arg]['title']), inline=False)
                            discordEmbed.set_thumbnail(url=songImageUrl)
                            msg = await ctx.send(embed=discordEmbed)
                            await msg.add_reaction(reaction)
                            timerEmojis = ['🕛', '🕒', '🕕' ,'🕘', '🕛']
                            for emoji in timerEmojis:
                                await msg.add_reaction(emoji)
                                await asyncio.sleep(2)
                                await msg.clear_reaction(emoji)
                            votes = 0
                            message = await ctx.channel.fetch_message(msg.id)
                            for i in message.reactions:
                                votes += i.count
                            requiredVotes = x*0.67
                            if votes > requiredVotes:
                                await msg.delete()
                                await ctx.send("**Song Removed Successfully**")
                                del botmain.song_queue[arg]
                            else:
                                await msg.delete()
                                await ctx.send("**Vote Failed!**")
                        else:
                            arg = arg - 1
                            await ctx.send("**{}** has been removed from the queue".format(botmain.song_queue[arg]['title']))
                            del botmain.song_queue[arg]
                            
                else:
                    await ctx.send("**You must be in the same VC as me to begin a vote!**")
            else:
                await ctx.send("**I'm not currently playing any music!**")

def setup(bot: commands.Bot):
    bot.add_cog(remove(bot))