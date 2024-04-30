import discord
from redbot.core import commands

class d2tzconv(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def d2tzconv(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("This might actually do something one day.")