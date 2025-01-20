
import discord, json, requests
from urllib.parse import quote
from redbot.core import commands
from redbot.core.utils.chat_formatting import box

class nbnco(commands.Cog):
    """Commands to pull data straight from the NBNCo Places API"""

    @commands.command()
    async def nbnco(self, ctx):
        """Commands to pull data straight from the NBNCo Places API"""
        __version__ = "0.0.1"
        __author__ = "deanosim"

    @commands.group()
    async def nbnco(self, ctx):
            "Group for NBNCo commands."

    @nbnco.command(name="details")
    async def details(self, ctx, locid):
            """Check NBN Places API for LocID details"""
            base_url = 'https://places.nbnco.net.au/places/v2/details/'

            if locid is not None:
                try:
                    url = ''.join([base_url, locid])
                except Exception:
                    return await ctx.send(
                        "An error has occured, did you include your LOC ID?"
                    )

            NBNDetailsData = requests.get(url, headers = {"referer": "https://www.nbnco.com.au/"})

            parsedDetails = json.loads(NBNDetailsData.text)
            msg = json.dumps(parsedDetails, indent=4)
            embed = discord.Embed(
                title=f"Results for **Details**",
                description=box(msg, lang="json")
            )
            await ctx.send(embed=embed)

    @nbnco.command()
    async def lookup(self, ctx, address):
            """Find your NBN Loc ID with your Address 'nbnco lookup "Address"`"""
            lookup_url = 'https://places.nbnco.net.au/places/v1/autocomplete?query='

            if address is not None:
                try:
                    encodedaddress = quote(address)
                    url = ''.join([lookup_url, encodedaddress])
                except Exception:
                    return await ctx.send(
                        "An error has occured, did you type your address correctly? `nbnco lookup 'Address'`"
                    )
            NBNLookupData = requests.get(url, headers = {"referer": "https://nbnco.com.au"})

            parsedLookup = json.loads(NBNLookupData.text)
            msg = json.dumps(parsedLookup, indent=4)
            embed = discord.Embed(
                title=f"Results for **Lookup**",
                description=box(msg, lang="json")
            )
            await ctx.send(embed=embed)