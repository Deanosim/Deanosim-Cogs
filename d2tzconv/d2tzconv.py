import discord
import datetime
from redbot.core import commands

class d2tzconv(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def d2tzconv(self, ctx):
        """This does stuff!"""

            # Get the current datetime
        py_dt = datetime.datetime.now()

        # Convert the datetime to an epoch timestamp (rounded to the nearest second)
        epoch = round(py_dt.timestamp())

        # Create the Discord timestamp string
        disc_dt = f"<t:{epoch}:R>"

        # Your code will go here
        await ctx.send("This might actually do something one day.")
        await ctx.send(disc_dt)
        

