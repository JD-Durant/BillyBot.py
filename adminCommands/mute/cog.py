import discord
import asyncio
import re
from discord.ext import commands
import sys
import traceback

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time


class mute(commands.Cog):
    """A | Mutes target user"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member:discord.Member=None, *, time:TimeConverter = None):
        """?mute {@user} {Optional : time (S/M/H/D)}"""
        if member is None:
            await ctx.send("**Please enter a valid target user!**")
            return
        await member.add_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
        await ctx.send(("**Muted {} for `{}s`!**" if time else "**Muted {}! (use ?unmute to reverse!)**").format(member, time))
        if time:
            await asyncio.sleep(time)
            await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
            await ctx.send(("**{} has been unmuted!**".format(member)))

        
def setup(bot: commands.Bot):
    bot.add_cog(mute(bot))