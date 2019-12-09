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
        await ctx.send("World Domination is near!")
        await ctx.send(datetime.time.strftime("Current Date and time is: %Y-%m-%d %H:%M:%S"))