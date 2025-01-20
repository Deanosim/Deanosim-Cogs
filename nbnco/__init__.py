from .nbnco import nbnco

async def setup(bot):
   await bot.add_cog(nbnco())