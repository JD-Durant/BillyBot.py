from discord.ext import commands
import discord
import asyncio
import datetime

class lockchannel(commands.Cog, name="lockChannel"):
    """A | Locks target channel"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['lockdown', 'lockchannel'])
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, channel: discord.TextChannel = None, reason: str = None, role: discord.Role = None):
        """Use prefix ?lock {channel} {reason} {Optional : target role}"""
        if channel is None:
            channel = ctx.channel
        else:
            channel = channel
        if role is None:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False, read_messages=True, view_channel=True)
            role = discord.utils.get(ctx.guild.roles, name="everyone")
        else:
            role = discord.utils.get(ctx.guild.roles, name=role.name)
            await channel.set_permissions(role, send_messages=False, add_reactions=False)
        if reason is None:
            reason = "No reason given"
        embed = discord.Embed(title="Channel locked",description=f"This channel was locked by {ctx.author.mention} 🔒",color=0x00fc8a)
        embed.add_field(name="Reason", value=reason.capitalize(), inline=True)
        embed.add_field(name="Roles affected", value=role, inline=True)
        embed.add_field(name="Channel affected", value=channel, inline=True)
        embed.add_field(name=":warning: | Important", value="**Users with Administrator perms won't be affected**", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)

        
def setup(bot: commands.Bot):
    bot.add_cog(lockchannel(bot)) 