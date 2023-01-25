import discord
from utils import Bot


bot = Bot(
    token="abc123",
    debug_logs=False,
    intents=discord.Intents.default()
)

if __name__ == '__main__':
    bot.load_subdir('cogs')

    bot.exec()
