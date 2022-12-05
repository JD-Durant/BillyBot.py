from discord.ext import commands
import discord
import datetime, time
import random
import asyncio

class russianRoulette(commands.Cog, name="russianRoulette"):
    """F | Russian Roulette"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    def create_embed(self, ctx, embedTitle, fieldOneTitle, fieldOneText):
        discordEmbed = discord.Embed(title="{}".format(embedTitle),description="{} vs {}".format(ctx.author.mention, '<@940105098942627860>'), color=0x00fc8a)
        discordEmbed.add_field(name="{}".format(fieldOneTitle), value="{}".format(fieldOneText), inline=True)
        discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        discordEmbed.timestamp = datetime.datetime.utcnow()
        return discordEmbed
    
    @commands.cooldown(1, 20, commands.BucketType.user)
    @commands.command(aliases=['rr'])
    async def russianRoulette(self, ctx: commands.Context, bullets:int=None):
        """?russianRoulette {optional : bullets} (default 1)"""
        barrel = []
        round = 1
        if bullets is None:
            barrel = ['click','click','click','click','click','bang']
            bullets = 1
        else:
            if bullets > 6:
                await ctx.send("Chamber only holds 6 bullets!")
                return
            elif bullets <= 0:
                await ctx.send("So.... no bullets? https://cdn.discordapp.com/attachments/992376000107266058/1005586485896020028/61vugl.jpg")
                return
            elif bullets == 6:
                await ctx.send("Bro like... do you need to like... talk to someone?")
                return
            else:
                barrel += bullets * ['bang']
                while len(barrel) != 6:
                    barrel.append('click')
        coinFlip = random.choice(["Heads!", "Tails!"])
        discordEmbed = discord.Embed(title="Setting up game",description="", color=0x00fc8a)
        discordEmbed.add_field(name="Spinning chamber 🔫", value="** **", inline=False)
        discordEmbed.add_field(name="Flipping :coin:", value="** **", inline=False)
        discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        discordEmbed.timestamp = datetime.datetime.utcnow()
        embedMessage = await ctx.send(embed=discordEmbed)
        await asyncio.sleep(3)
        player = None
        if coinFlip == "Heads!":
            player = "billy"
            await embedMessage.edit(embed=self.create_embed(ctx, f"{coinFlip}", "Billy goes first", "** **"))
        else:
            await embedMessage.edit(embed=self.create_embed(ctx, f"{coinFlip}", "User goes first", "** **"))
        await asyncio.sleep(3)
        while True:
            if player == "billy":
                await embedMessage.edit(embed=self.create_embed(ctx, f"Round {round} | {bullets} bullets in the chamber", "Billy's Turn", "Billy is now choosing"))
                barrelChoice = random.choice(barrel)
                await asyncio.sleep(3)
                if barrelChoice == 'bang':
                    await embedMessage.edit(embed=self.create_embed(ctx, "💥 🔫", "Player Wins!", "👑👑👑"))
                    await ctx.message.add_reaction('🏆')
                    break
                else:
                    barrel.remove('click')
                    await embedMessage.edit(embed=self.create_embed(ctx, "Billy is safe! 😅", "Passing to user", "GL!"))
                    await asyncio.sleep(4)
                    round = round + 1
                    player = "user"
            else:
                choiceEmojis = ['🏃', '🔫']
                await embedMessage.edit(embed=self.create_embed(ctx, f"Round {round} | {bullets} bullets in the chamber", "Users turn", "Waiting for user to choose"))
                for emoji in choiceEmojis:
                    await embedMessage.add_reaction(emoji)
                timerEmojis = ['🕛', '🕒', '🕕' ,'🕘', '🕛']
                for emoji in timerEmojis:
                    await embedMessage.add_reaction(emoji)
                    await asyncio.sleep(1)
                    await embedMessage.clear_reaction(emoji)
                message = await ctx.channel.fetch_message(embedMessage.id)
                users = set()
                for reaction in message.reactions:
                    async for user in reaction.users():
                        users.add(user)
                userReactedTo = None
                if any(reaction.emoji in choiceEmojis for reaction in message.reactions):
                    for i in message.reactions:
                        if i.count >= 2:
                            for user in users:
                                if ctx.author.id == user.id:
                                    if userReactedTo is None:
                                        userReactedTo = str(i)
                                    else:
                                        await embedMessage.edit(embed=self.create_embed(ctx, "Disqualified", "Reason", "Too many choices! 👎"))
                                        await embedMessage.clear_reactions()
                                        await embedMessage.add_reaction('👎')
                                        break
                if userReactedTo is None:
                    await embedMessage.edit(embed=self.create_embed(ctx, "Billy Wins!", "Reason", "User didn't choose anything!"))
                    await embedMessage.clear_reactions()
                    await embedMessage.add_reaction('👎')
                    break
                elif "🏃" in userReactedTo:
                    await embedMessage.edit(embed=self.create_embed(ctx, "Billy Wins!", "Reason", "User decided to run! Booo!"))
                    await embedMessage.clear_reactions()
                    await embedMessage.add_reaction('👎')
                    break
                elif "🔫" in userReactedTo:
                    barrelChoice = random.choice(barrel)
                    if barrelChoice == 'bang':
                        await embedMessage.edit(embed=self.create_embed(ctx, "💥 🔫", "Billy Wins!", "User was unlucky GG!"))
                        await embedMessage.clear_reactions()
                        await embedMessage.add_reaction('👎')
                        break
                    else:
                        barrel.remove('click')
                        await embedMessage.edit(embed=self.create_embed(ctx, "User is safe! 😅", "Passing to Billy", "GL!"))
                        await embedMessage.clear_reactions()
                        round = round + 1
                        await asyncio.sleep(4)
                        player = "billy"
                

def setup(bot: commands.Bot):
    bot.add_cog(russianRoulette(bot))