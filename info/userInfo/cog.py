from discord.ext import commands
import time
import discord
import random
import botmain
import datetime

class userInfo(commands.Cog, name="userInfo"):
    """I | Shows target user Info"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def userInfo(self, ctx, user:discord.Member = None):
        """?userinfo {optional : @user}"""
        if not user:
            user = ctx.author
        statusString = None
        roleString = "```\n"
        if str(user.status) == 'online':
            statusString = 'Online 🟢'
        elif str(user.status) == 'offline':
            statusString = 'Offline ⚫'
        elif str(user.status) == 'idle':
            statusString = 'Away 🟡'
        elif str(user.status) == 'dnd':
            statusString = 'Do Not Disturb 🔴'
        for role in user.roles:
            roleString += f"{role}\n"
        roleString += "\n```"
        dateFormat = "%a, %d/%b/%Y"
        discordEmbed = discord.Embed(title=f"{user.name}'s Info", description="", color=0x00fc8a)
        discordEmbed.add_field(name='📝 General Info', value = f"**Username** : {user.name} | Current Status : {statusString}", inline = False)
        discordEmbed.add_field(name='📆 Created On', value = f"{user.created_at.strftime(dateFormat)}", inline = True)
        discordEmbed.add_field(name='➡️ Joined On', value = f"{user.joined_at.strftime(dateFormat)}", inline = True)
        discordEmbed.add_field(name='🥇 Top Role', value = f'{user.top_role}', inline = False)
        discordEmbed.add_field(name='🔰 All Roles', value = f'{roleString}📏Total Roles : {len(user.roles)}', inline = False)
        discordEmbed.timestamp = datetime.datetime.utcnow()
        discordEmbed.set_author(name=str(user), icon_url=user.avatar_url)
        discordEmbed.set_thumbnail(url=user.avatar_url)
        discordEmbed.set_footer(text='User ID: ' + str(user.id))
        await ctx.send(embed=discordEmbed)

def setup(bot: commands.Bot):
    bot.add_cog(userInfo(bot))