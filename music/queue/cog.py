from discord.ext import commands
import discord
import botmain
import datetime

class queue(commands.Cog, name="queue"):
    """M | Displays all songs in current queue"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['q'])
    async def queue(self, ctx: commands.Context, *arg):
        """?queue {Optional : Queue position}"""
        if len(botmain.song_queue) == 0:
            await ctx.send("**Queue is currently empty!**")
        else:
            if not arg:
                queueLength = 0
                x = 1
                discordEmbed = discord.Embed(title="Current Queue", description="", color=0x00fc8a)
                for i in range(len(botmain.song_queue)):
                    if x > 10:
                        for i in range(x, len(botmain.song_queue)+1):
                            queueLength = queueLength + botmain.song_queue[i]['duration']
                        amountRemaining = len(botmain.song_queue)+1 - x
                        discordEmbed.add_field(name=f'And {amountRemaining} more!', value="** **", inline=False)
                        break
                    else:
                        queueLength = queueLength + botmain.song_queue[i]['duration']
                        discordEmbed.add_field(name='[{}]{}'.format(x, botmain.song_queue[i]['title']), value="Song Length : {}".format(str(datetime.timedelta(seconds=botmain.song_queue[i]['duration']))), inline=False)
                        x = x + 1 
                discordEmbed.set_footer(text="Total queue time : {} minutes".format(str(datetime.timedelta(seconds=queueLength))))
                discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                discordEmbed.set_thumbnail(url=botmain.song_queue[0]['url'])
                await ctx.send(embed=discordEmbed)
            else:
                try:
                    argQueueLength = int(arg[0])
                    argInt = argQueueLength - 1
                except ValueError as verr:
                    await ctx.send("**Please enter a number!**")
                    return
                if argQueueLength > len(botmain.song_queue):
                    await ctx.send("**There are not that many songs in queue!**")
                else:
                    discordEmbed = discord.Embed(title="{}".format(botmain.song_queue[argInt]['title']), url="{}".format(botmain.song_queue[argInt]['directurl']), description="", color=0x00fc8a)
                    discordEmbed.add_field(name="Song Length", value="{}".format(str(datetime.timedelta(seconds=botmain.song_queue[argInt]['duration']))), inline=True)
                    discordEmbed.add_field(name="Likes", value="{:,}".format(botmain.song_queue[argInt]['likes']), inline=True)
                    discordEmbed.add_field(name="Views", value="{:,}".format(botmain.song_queue[argInt]['views']), inline=True)
                    discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                    discordEmbed.timestamp = datetime.datetime.utcnow()
                    discordEmbed.set_thumbnail(url=botmain.song_queue[argInt]['url'])
                    await ctx.send(embed=discordEmbed)

def setup(bot: commands.Bot):
    bot.add_cog(queue(bot))