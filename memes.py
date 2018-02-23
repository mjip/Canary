#!/usr/bin/env python3

# discord-py requirements
from discord.ext import commands
import asyncio

# Other utilities
import random


class Memes():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def lenny(self, ctx):
        """
        Lenny face
        """
        yield from self.bot.send_message(ctx.message.channel, "( ͡° ͜ʖ ͡°) ")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def license(self, ctx):
        """
        License
        """
        yield from self.bot.send_message(ctx.message.channel, "This bot is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. **This bot is distributed in the hope that it will be useful**, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or **FITNESS FOR A PARTICULAR PURPOSE**.  See the GNU General Public License for more details. This bot is developed primarily by student volunteers with better things to do. A copy of the GNU General Public License is provided in the LICENSE.txt file along with this bot. The GNU General Public License can also be found at <http://www.gnu.org/licenses/>.")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def gohere(self, ctx):
        """
        for future mcgillians
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "http://gph.is/1cN9wO1")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def tunak(self, ctx):
        """
        bitch pls
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "http://i.imgur.com/rNNLyjK.gif")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def bb8(self, ctx):
        """
        nice job bb8
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "http://i.imgur.com/SUvaUM2.gif")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def longtime(self, ctx):
        """
        That's a name I've not heard in a long time
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "http://i.imgur.com/e1T1xcq.mp4")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def thonk(self, ctx):
        """
        when thonking consumes you
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "https://i.imgur.com/VADGUwj.gifv")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def dealwithit(self, ctx):
        """
        deal with it trump
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "http://i.imgur.com/5jzN8zV.mp4")
        yield from self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def lmao(self, ctx):
        """
        that's hilarious
        """
        yield from self.bot.send_message(ctx.message.channel,
                                         "http://i.imgur.com/o5Cc3i2.mp4")
        yield from self.bot.delete_message(ctx.message)

    @commands.command()
    @asyncio.coroutine
    def chirp(self):
        """:^)"""
        yield from self.bot.say('CHIRP CHIRP')

    @commands.command(pass_context=True)
    @asyncio.coroutine
    def mix(self, ctx, *, inputStr: str=None):
        if inputStr is None:
            yield from self.bot.say()
        msg = "".join([(c.upper() if
                        random.randint(0, 1) else
                        c.lower()) for c in inputStr])
        yield from self.bot.say(msg)
        yield from self.bot.delete_message(ctx.message)


def setup(bot):
    bot.add_cog(Memes(bot))
