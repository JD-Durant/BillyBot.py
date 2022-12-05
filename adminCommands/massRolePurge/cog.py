from discord.ext import commands
import discord

class rolepurge(commands.Cog, name="rolePurge"):
    """A | Mass role purge"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rolepurge(self, ctx: commands.Context, role: discord.Role=None):
        """?rolepurge {@role}"""
        if role is None:
            await ctx.send("**Please enter a valid role!**")
            return
        counter = 0
        role = discord.utils.get(ctx.guild.roles, name=role.name)
        for user in ctx.guild.members:
            if role in user.roles:
                await user.remove_roles(role)
                counter = counter + 1
        if counter == 0:
            await ctx.send("**There is no-one with that role!**")
        else:
            await ctx.send("**Done ! Removed ``{}`` role from ``{} members`` {}**".format(role.name, counter, ctx.author.mention))

def setup(bot: commands.Bot):
    bot.add_cog(rolepurge(bot))