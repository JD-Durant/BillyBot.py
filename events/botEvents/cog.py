from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
import datetime
import discord
import botmain
import random
import asyncio
from discord.ext.commands import cooldown, BucketType

class botEvents(commands.Cog):
    """IGNORE | Bot Listeners"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        if botmain.devMode == True:
            await self.client.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity(type=discord.ActivityType.listening, name="Josh swear at code"))
            print(f"{self.client.user.name} has connected to Discord in Dev Mode.")
        else:
            self.statusTask.start()
            print(f"{self.client.user.name} has connected to Discord.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        splitMessage = list(ctx.message.content)
        if splitMessage[1] == '?':
            return
        if isinstance(error, CommandNotFound):
            await ctx.send("**'{}' is not a known command! {}**".format(ctx.message.content, ctx.author.mention))
            return
        elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
            await ctx.send("**You do not have permission to use that command!**")
            return
        elif isinstance(error, (commands.MissingPermissions)):
            await ctx.send("**You do not have permission to use that command!**")
            return
        elif isinstance(error, commands.CommandOnCooldown):
            discordEmbed = discord.Embed(title=f"Whoa! Slow down there!",description=f"Try again in {error.retry_after:.1f}s ⏱️", color=0xFFB347)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=discordEmbed)
            return

def setup(bot):
    bot.add_cog(botEvents(bot))