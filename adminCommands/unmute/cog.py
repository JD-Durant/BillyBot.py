from discord.ext import commands
import discord

class unmute(commands.Cog, name="unmute"):
    """A | Unmutes targeted user"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx: commands.Context, user: discord.Member=None):
        """?unmute {@user}"""
        if user is None:
            await ctx.send("**Please enter a valid target user!**")
            return
        if discord.utils.get(ctx.guild.roles, name="Muted") not in user.roles:
            await ctx.send("**<@{}> is not currently muted!**".format(user.id))
            return
        else:
            await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
            await ctx.send("**<@{}> has been unmuted!**".format(user.id))

        
def setup(bot: commands.Bot):
    bot.add_cog(unmute(bot))