import discord
from discord.ext import commands

from config import DISCORD_TOKEN, COMMAND_PREFIX

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

async def main():
    await bot.load_extension("cogs.stocks")
    await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())






