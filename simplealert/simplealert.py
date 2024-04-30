import asyncio
import time
import datetime

import discord
from redbot.core import commands
from datetime import datetime

class simplealert(commands.Cog):
    """My custom cog"""


    @commands.command()
    async def simplealert(self, ctx):
        """This does stuff!"""
        # Your code will go here
        fmt = "**%Y-%m-%d %H:%M:%S**"
        time = time.strftime(fmt)
        await ctx.send("World Domination is near!")
        await ctx.send(f"{str(time)}")