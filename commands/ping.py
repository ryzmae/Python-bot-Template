import discord
from discord.ext import commands
from colorama import Fore

class pingcommand(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")
        
def setup(bot):
    bot.add_cog(pingcommand(bot))