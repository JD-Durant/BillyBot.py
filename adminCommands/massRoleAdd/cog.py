from discord.ext import commands
import discord

class roleadd(commands.Cog, name="roleAdd"):
    """A | Mass role add"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roleadd(self, ctx: commands.Context, role: discord.Role=None):
        """?roleadd {@role}"""
        if role is None:
            await ctx.send("**Please enter a valid role!**")
            return
        counter = 0
        role = discord.utils.get(ctx.guild.roles, name=role.name)
        for user in ctx.guild.members:
            if role not in user.roles:
                await user.add_roles(role)
                counter = counter + 1
        if counter == 0:
            await ctx.send("**Everyone already has that role!**")
        else:
            await ctx.send("**Done ! Added ``{}`` role to ``{} members`` {}**".format(role.name, counter, ctx.author.mention))

def setup(bot: commands.Bot):
    bot.add_cog(roleadd(bot))