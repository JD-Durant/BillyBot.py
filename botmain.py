import os
from discord.ext import commands, tasks
import discord
import datetime, time
songList = []
songList = [line.strip() for line in open("Text Files/statusSongLinks.txt", 'r')]
intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents, case_insensitive=True, help_command=None)
from dotenv import load_dotenv
clientID = os.getenv('SPOTIFYCLIENTID')
clientSecret = os.getenv('SPOTIFYCLIENTSECRET')
load_dotenv()
song_queue = []
recentlyplayed = []
song_start = 0
startTime = time.mktime(datetime.datetime.today().timetuple())
devMode = False
currentVoiceGuild = None
version = "3.2.1"
durationError = 0
searchError = False

def main():
    load_dotenv()

    for folder in os.listdir("adminCommands"):  
        if os.path.exists(os.path.join("adminCommands", folder, "cog.py")):
            client.load_extension(f"adminCommands.{folder}.cog")
    for folder in os.listdir("fun"):
        if os.path.exists(os.path.join("fun", folder, "cog.py")):
            client.load_extension(f"fun.{folder}.cog")
    for folder in os.listdir("music"):
        if os.path.exists(os.path.join("music", folder, "cog.py")):
            client.load_extension(f"music.{folder}.cog")
    for folder in os.listdir("events"):  
        if os.path.exists(os.path.join("events", folder, "cog.py")):
            client.load_extension(f"events.{folder}.cog")
    for folder in os.listdir("info"):  
        if os.path.exists(os.path.join("info", folder, "cog.py")):
            client.load_extension(f"info.{folder}.cog")

    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)

if __name__ == '__main__':
    main()