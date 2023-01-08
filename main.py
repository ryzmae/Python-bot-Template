# Importing modules
import discord, os
from discord.ext import commands
from colorama import Fore

# Defining the bot
prefix = "?" # Your prefix here
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=intents, help_command=None)
token = "" # Your token here

@client.event
async def on_ready():
    print(f"{Fore.GREEN}Bot is ready!")
    
# command Handler
if __name__ == "__main__":
    for filename in os.listdir("commands"):
        if filename.endswith(".py"):
            client.load_extension(f"commands.{filename[:-3]}")

    client.run(f"{token}") # Running the bot