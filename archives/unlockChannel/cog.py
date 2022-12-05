from discord.ext import commands
import discord
import asyncio
import datetime

class unlockchannel(commands.Cog, name="unlockchannel"):
    """Recieves commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None, role: discord.Role = None):
        if channel is None:
            channel = ctx.channel
        else:
            channel = channel
        if role is None:
            await channel.set_permissions(ctx.guild.default_role, send_messages=True, add_reactions=True, read_messages=True, view_channel=True)
        else:
            role = discord.utils.get(ctx.guild.roles, name=role.name)
            await channel.set_permissions(role, send_messages=True, add_reactions=True)
        embed = discord.Embed(title="Channel unlocked",description=f"This channel was locked by {ctx.author.mention} 🔒",color=0x00fc8a)
        embed.add_field(name="Roles affected", value=role.name, inline=True)
        embed.add_field(name="Channel affected", value=channel, inline=True)
        embed.add_field(name=":warning: | Important", value="**Users with Administrator perms won't be affected**", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)

        
def setup(bot: commands.Bot):
    bot.add_cog(unlockchannel(bot))