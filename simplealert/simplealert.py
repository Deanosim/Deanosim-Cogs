
import discord
from redbot.core import commands

class simplealert(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def simplealert(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("World Domination is near!")