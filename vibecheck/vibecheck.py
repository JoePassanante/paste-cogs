import asyncio
import io
import re
import datetime
import time
from collections import namedtuple

import aiohttp
import discord
from redbot.core import Config, checks, commands
from redbot.core.utils.chat_formatting import box, pagify

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

BaseCog = getattr(commands, "Cog", object)

class Vibecheck(BaseCog):
    """Check them vibes"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=974374574)
        default_guild = {}
        self.config.register_guild(**default_guild)
        self.config.register_user(vibe=0)
        self.config.register_user(lastran=datetime.date)

    @commands.command()
    async def vibecheck(self, ctx: commands.Context):
        """Check your vibes"""
        today = date.today()
        last = await self.config.user(member).lastran()

        await ctx.send(today)
        await ctx.send(last)

        vibe = randint(1, 20)

        if vibe == 1:
            comment = "lmaooo"
        elif vibe < 6:
            comment = "Sucks for you bro"
        elif vibe < 11:
            comment = "I guess that's fine"
        elif vibe < 16:
            comment = "Pretty sick dude"
        elif vibe < 20:
            comment = "Vibin hard"
        else:
            comment = "Okay King"

        await ctx.send(":game_die: {} checked their vibe and got {}\n{}".format(
            ctx.message.author.mention,vibe,comment)
        )