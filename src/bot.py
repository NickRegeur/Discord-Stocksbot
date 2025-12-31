import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv


async def main():
    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} (id={bot.user.id})")

    await bot.load_extension("cogs.stocks")
    await bot.start(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    asyncio.run(main())






