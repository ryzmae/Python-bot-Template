import discord
from discord.ext import commands
from discord.commands import slash_command


class PingCommand(commands.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot = bot

    @slash_command(name="ping", description="Pong")
    async def ping(self, ctx: discord.ApplicationContext) -> None:
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot: discord.Bot) -> None:
    bot.add_cog(PingCommand(bot))
