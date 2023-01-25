import discord
from discord.ext import commands


class OnReady(commands.Cog):

    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"{self.bot.user} is online")


def setup(bot: discord.Bot) -> None:
    bot.add_cog(OnReady(bot))
