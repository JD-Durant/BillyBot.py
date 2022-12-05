from discord.ext import commands
import discord
import botmain

class amiplaying(commands.Cog, name="amiplaying"):
    """I | Shows if bot is playing music"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['playing'])
    async def amiplaying(self, ctx: commands.Context):
        """?amiplaying"""
        if botmain.currentVoiceGuild == None:
            await ctx.message.reply("**I am not currently playing in another server! {}**".format(ctx.author.mention))
        elif botmain.currentVoiceGuild == ctx.guild:
            await ctx.message.reply("**I am currently playing in this server! {}**".format(ctx.author.mention))
        else:
            await ctx.message.reply("**I am currently playing in another server!! {}**".format(ctx.author.mention))
        
def setup(bot: commands.Bot):
    bot.add_cog(amiplaying(bot))