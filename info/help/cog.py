from discord.ext import commands
import discord
import datetime
import botmain
from discord import Embed

class help(commands.Cog, name="help"):
    """I | Displays this command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def help(self, ctx: commands.Context, *input):
        """Bruuh u dum as hell"""
        prefix = "?"
        if not input:
            discordEmbed = discord.Embed(title='Help', url="https://www.sanfransentinel.com/billy-bot-fq.html", description=f'Use `{prefix}help <module>` to see how to use a command!', color=0x00fc8a)
            admin_cogs_desc = '```ini\n'
            fun_cogs_desc = '```ini\n'
            info_cogs_desc = '```ini\n'
            music_cogs_desc = '```ini\n'
            for cog in self.bot.cogs:
                if 'A | ' in self.bot.cogs[cog].__doc__:
                    admin_cogs_desc += f'[{cog}] : {self.bot.cogs[cog].__doc__.strip("A | ")}\n'
                if 'F | ' in self.bot.cogs[cog].__doc__:
                    fun_cogs_desc += f'[{cog:}] : {self.bot.cogs[cog].__doc__.strip("F | ")}\n'
                elif 'I | ' in self.bot.cogs[cog].__doc__:
                    info_cogs_desc += f'[{cog:}] : {self.bot.cogs[cog].__doc__.strip("I | ")}\n'
                elif 'M | ' in self.bot.cogs[cog].__doc__:
                    music_cogs_desc += f'[{cog:}] : {self.bot.cogs[cog].__doc__.strip("M | ")}\n'
                else:
                    pass
            admin_cogs_desc+='\n```'
            fun_cogs_desc+='\n```'
            info_cogs_desc+='\n```'
            music_cogs_desc+='\n```'
            discordEmbed.add_field(name='Admin Modules / Commands', value=admin_cogs_desc, inline=False)
            discordEmbed.add_field(name='Info Modules / Commands', value=info_cogs_desc, inline=False)
            discordEmbed.add_field(name='Fun Modules / Commands', value=fun_cogs_desc, inline=False)
            discordEmbed.add_field(name='Music Modules / Commands', value=music_cogs_desc, inline=False)
            commands_desc = ''
            if commands_desc:
                discordEmbed.add_field(name='Not belonging to a module', value=commands_desc, inline=False)
            discordEmbed.set_footer(text=f"Bot is running {botmain.version}")
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/992376000107266058/1004438333239337070/1211.jpg')
        elif len(input) == 1:
            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():
                    discordEmbed = discord.Embed(title=f'{cog} - Commands', url="https://www.sanfransentinel.com/billy-bot-fq.html", description=self.bot.cogs[cog].__doc__, color=0x00fc8a)
                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            discordEmbed.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/992376000107266058/1004438333239337070/1211.jpg')
        elif len(input) > 1:
            discordEmbed = discord.Embed(title="Don't be greedy!", description="Please request only one module at a time!", color=0x8D021F)
        await ctx.send(embed=discordEmbed)
            

def setup(bot: commands.Bot):
    bot.add_cog(help(bot))