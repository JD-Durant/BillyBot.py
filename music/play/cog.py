import asyncio
import botmain
from spotipy.oauth2 import SpotifyClientCredentials
from discord.ext import commands
from discord.utils import get
import discord
from yt_dlp import YoutubeDL
import time
import requests
import datetime
import random
import spotipy
thinkMessages = []
thinkMessages = [line.strip() for line in open("Text Files/ThinkMessages.txt", 'r')]
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 4294', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'quiet': True, 'extract-audio': True, 'skip_download': True, 'ignore-errors': True, 'sleep-requests' : 1}
client_credentials_manager = SpotifyClientCredentials(client_id=botmain.clientID, client_secret=botmain.clientSecret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
tempSearchList = []

class play(commands.Cog, name="play"):
    """M | Plays music"""
        
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    def search(self, arg):
        try: requests.get("".join(arg))
        except: arg = " ".join(arg)
        else: arg = "".join(arg)

        with YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
                song = {'source': info['url'], 'title': info['title'], 'duration': info['duration'], 'url' : info['thumbnail'], 'directurl' : info['webpage_url'], 'views' : info['view_count'], 'likes' : info['like_count']}
                if int(song['duration']) > 7200:
                    botmain.durationError = True
                    return
                else:
                    botmain.song_queue.append(song)
                    return
            except:
                botmain.searchError = True
                return True

    def play_next(self, ctx, *arg):
        voice: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if len(botmain.recentlyplayed) >= 5:
            del botmain.recentlyplayed[0]
        botmain.recentlyplayed.append(botmain.song_queue[0])
        del botmain.song_queue[0]
        botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
        if len(botmain.song_queue) > 0:
            voice.play(discord.FFmpegPCMAudio(botmain.song_queue[0]['source'], **FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
        else:
            return
        
    def create_embed(self, ctx, playType, songName, songLengthMins, songUrl, playlist=None):
        if playlist is None:
            discordEmbed = discord.Embed(title=playType, description="", color=0x00fc8a)
            discordEmbed.add_field(name="{}".format(songName), value="Song Length : {}".format(songLengthMins), inline=False)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_thumbnail(url=songUrl)
            return discordEmbed
        else:
            discordEmbed = discord.Embed(title=playType, description="", color=0x00fc8a)
            discordEmbed.add_field(name="{}".format(songName), value="{}".format(songLengthMins), inline=False)
            discordEmbed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
            discordEmbed.timestamp = datetime.datetime.utcnow()
            discordEmbed.set_thumbnail(url=songUrl)
            return discordEmbed
    
    def spotifySearch(self, arg):
        searchQuery = str(arg)
        if "/playlist" in searchQuery:
            playlist_URI = searchQuery.split("/")[-1].split("?")[0]
            for track in sp.playlist_tracks(playlist_URI)["items"]:
                tempSearchList.append("{} {}".format(track["track"]["name"], track["track"]["artists"][0]["name"]))
            return
        else:
            searchQueryURI = searchQuery.split("/")[-1].split("?")[0]
            seachResult = sp.track(searchQueryURI)
            self.search("{} {}".format(seachResult["name"], seachResult["artists"][0]["name"]))
            return

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def play(self, ctx: commands.Context, *arg):
        """?play {song name/link}"""
        playListDetected = False
        playlistQueueLength = 0
        if ctx.author.voice and ctx.author.voice.channel:
            voiceChannel = ctx.message.author.voice.channel
        else:
            await ctx.send("**You are not connected to voice!**")
            return
        if botmain.currentVoiceGuild is not None:
            if botmain.currentVoiceGuild != ctx.guild:
                await ctx.send("Sorry! I am currently playing in another server!")
                return
        if discord.utils.get(ctx.guild.roles, name="Muted") in ctx.author.roles:
            await ctx.send("**You are currently blacklisted!**")
            return
        if not arg:
            await ctx.send("**Please enter a valid song!**")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if "open.spotify.com" in str(arg):
            if "/playlist" in str(arg):
                self.spotifySearch(arg)
                if len(tempSearchList) > 10:
                    await ctx.send("That's too many songs for me to handle! Please use a playlist with less than 10 songs!")
                    tempSearchList.clear()
                    return
                thinkingMessage = await ctx.send("Spotify playlist detected. Please wait, this may take some time. Loading : `{}` songs".format(len(tempSearchList)))
                skippedSongs = []
                for i in range(len(tempSearchList)):
                    self.search("{}".format(tempSearchList[i]))
                    if botmain.durationError == True:
                        skippedSongs.append(i)
                        botmain.durationError = False
                        return
                if skippedSongs:
                    await thinkingMessage.edit(content="Skipping following songs due to length being over 2 hours {}".format(skippedSongs))
                    asyncio.sleep(2)
                playListDetected = True
                playlistQueueLength = len(tempSearchList)
                tempSearchList.clear()
            else:
                thinkingMessage = await ctx.send("{}".format(random.choice(thinkMessages)))
                self.spotifySearch(arg)
        else:
            thinkingMessage = await ctx.send("{}".format(random.choice(thinkMessages)))
            self.search(arg)
        if botmain.durationError == True:
            await thinkingMessage.edit(content="Sorry! Im not playing a song over **2 hours** in length! {}".format(ctx.author.mention))
            botmain.durationError = False
            return
        if botmain.searchError == True:
            await thinkingMessage.edit(content="**Sorry! There was an unexpected error (check if the video / song is age restricted)**")
            botmain.searchError = False
            return
        if voice and voice.is_connected():
            await voice.move_to(voiceChannel)
        else:
            voice = await voiceChannel.connect()
            botmain.currentVoiceGuild = ctx.guild
        if not voice.is_playing():
            if playListDetected == False:
                if len(botmain.song_queue) > 1:
                    botmain.song_queue.clear()
            voice.play(discord.FFmpegPCMAudio(botmain.song_queue[0]['source'], before_options='-reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 4294', options='-vn'), after=lambda e: self.play_next(ctx))
            await thinkingMessage.delete()
            if playListDetected == False:
                await ctx.send(embed=self.create_embed(ctx, "Now Playing", botmain.song_queue[-1]['title'], str(datetime.timedelta(seconds=botmain.song_queue[-1]['duration'])), botmain.song_queue[-1]['url']))
                botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
            else:
                await ctx.send(embed=self.create_embed(ctx, "Spotify Playlist Queued", "Songs queue", "Successfully queued `{}` songs".format(playlistQueueLength), botmain.song_queue[-1]['url'], True))
                botmain.song_start = time.mktime(datetime.datetime.today().timetuple())
        else:
            if playListDetected == False:
                await thinkingMessage.delete()
                await ctx.send(embed=self.create_embed(ctx, "Queued", botmain.song_queue[-1]['title'], str(datetime.timedelta(seconds=botmain.song_queue[-1]['duration'])), botmain.song_queue[-1]['url']))
            else:
                await thinkingMessage.delete()
                await ctx.send(embed=self.create_embed(ctx, "Spotify Playlist Queued", "Songs queue", "Successfully queued `{}` songs".format(playlistQueueLength), botmain.song_queue[-1]['url'], True))

def setup(bot: commands.Bot):
    bot.add_cog(play(bot))