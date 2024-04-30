from .d2tzconv import d2tzconv

async def setup(bot):
   await bot.add_cog(d2tzconv())