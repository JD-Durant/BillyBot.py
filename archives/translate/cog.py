from discord.ext import commands
import discord
from googletrans import Translator, constants

class translate(commands.Cog, name="translate"):
    """Translates given text"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def translate(self, ctx: commands.Context, targetLanguage=None, *arg):
        """?translate {target language code} {text}"""
        translator = Translator()
        if targetLanguage is None:
            trans = translator.translate('{}'.format(arg), dest='en')
            discordEmbed = discord.Embed(title="Translation", description="", color=0x00fc8a)
            discordEmbed.add_field(name="Input", value="{} | {}".format(trans.src ,trans.origin), inline=False)
            discordEmbed.add_field(name="Output", value="{} | {}".format(trans.dest, trans.text))
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=discordEmbed)
        else:
            trans = translator.translate('{}'.format(arg), dest=targetLanguage)
            discordEmbed = discord.Embed(title="Translation", description="", color=0x00fc8a)
            discordEmbed.add_field(name="Input", value="{} | {}".format(trans.src ,trans.origin), inline=False)
            discordEmbed.add_field(name="Output", value="{} | {}".format(trans.dest, trans.text))
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=discordEmbed)
            

def setup(bot: commands.Bot):
    bot.add_cog(translate(bot))