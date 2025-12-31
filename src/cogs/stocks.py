from discord.ext import commands
from services.stock_data import get_quote


class Stocks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="quote")
    async def quote(self, ctx: commands.Context, symbol: str):

        try:
            q = get_quote(symbol)
        except Exception as e:
            await ctx.send(f"Couldn't fetch `{symbol}`: {e}")
            return

        lines = [
            f"**{q.symbol}**: `{q.price:.2f} {q.currency}`",
        ]

        if q.change is not None and q.change_percent is not None:
            sign = "+" if q.change >= 0 else ""
            lines.append(f"Change: `{sign}{q.change:.2f}` ({sign}{q.change_percent:.2f}%)")

        await ctx.send("\n".join(lines))


async def setup(bot: commands.Bot):
    await bot.add_cog(Stocks(bot))
