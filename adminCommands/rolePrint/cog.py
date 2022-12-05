from discord.ext import commands
import discord
import datetime

class roleprint(commands.Cog, name="rolePrint"):
    """A | Prints all user under target role"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['rolecount'])
    @commands.has_permissions(administrator=True)
    async def roleprint(self, ctx: commands.Context, role: discord.Role=None):
        """?roleprint {Optional : @role}"""
        if role is None:
            roles = await ctx.guild.fetch_roles()
            discordEmbed = discord.Embed(title="Total for each role", description="", color=0x00fc8a)
            x = 0
            embedString = "```ini\n"
            for role in roles:
                i = 0
                for user in ctx.guild.members:
                    if role in user.roles:
                        i = i + 1
                embedString+=f"[ {role.name} ] : {i}\n"
                x = x + i
            embedString+='\n```'
            discordEmbed.add_field(name='** **', value=f"{embedString}", inline=False)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_footer(text = "Total : {}".format(x), icon_url = "https://cdn.discordapp.com/attachments/992376000107266058/1004060081521967184/imageedit_2_5612939050.jpg")
            await ctx.send(embed=discordEmbed)
        else:
            i = 1
            discordEmbed = discord.Embed(title="Users with {} Role".format(role.name), description="", color=0x00fc8a)
            role = discord.utils.get(ctx.guild.roles, name=role.name)
            embedString = "```"
            for user in ctx.guild.members:
                if role in user.roles:
                    userString = f"{i: <2} | @{user}\n"
                    embedString+=userString
                    i = i + 1
            embedString+="```"
            discordEmbed.add_field(name=f'{role.name}', value=embedString, inline=False)
            if i == 1:
                await ctx.send("**There is no-one with that role!**")
            else:
                discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
                discordEmbed.timestamp = datetime.datetime.utcnow()
                discordEmbed.set_footer(text = "Total : {}".format(i-1), icon_url = "https://cdn.discordapp.com/attachments/992376000107266058/1004060081521967184/imageedit_2_5612939050.jpg")
                await ctx.send(embed=discordEmbed)

        
def setup(bot: commands.Bot):
    bot.add_cog(roleprint(bot))