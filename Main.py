#!/usr/bin/env python3

# discord-py requirements
import discord
from discord.ext import commands
import asyncio

#for database
import sqlite3

# logger
import logging

# Other utilities
import os, sys

# List the extensions (modules) that should be loaded on startup.
startup = ["db", "memes", "helpers"]
DB_PATH = './Martlet.db'

bot = commands.Bot(command_prefix='?')

# Logging configuration
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode = 'w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
@asyncio.coroutine
def on_ready():
    print('Logged in as {0} ({1})'.format(bot.user.name, bot.user.id))


@bot.command(pass_context=True)
@commands.has_role("Discord Moderator")
@asyncio.coroutine
def load(ctx, extension_name: str):
    '''
    Load a specific extension.
    '''
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        yield from ctx.send("```{}: {}\n```".format(type(e).__name__, str(e)))

        return
    yield from ctx.send("{} loaded.".format(extension_name))


@bot.command(pass_context=True)
@commands.has_role("Discord Moderator")
@asyncio.coroutine
def unload(ctx, extension_name: str):
    '''
    Unload a specific extension.
    '''
    bot.unload_extension(extension_name)
    yield from ctx.send("Unloaded {}.".format(extension_name))


@bot.command(pass_context=True)
@asyncio.coroutine
def restart(ctx):
    '''
    Restart the bot
    '''
    yield from ctx.send('https://streamable.com/dli1')
    python = sys.executable
    os.execl(python, python, *sys.argv)


@bot.command(pass_context=True)
@asyncio.coroutine
def update(ctx):
    '''
    Update the bot by pulling changes from the git repository
    '''
    yield from ctx.send('https://streamable.com/c7s2o')
    os.system('git pull')


@bot.event
@asyncio.coroutine
def on_reaction_add(reaction,user):
    # Check for Martlet emoji + upmartletting yourself
    if not reaction.custom_emoji:
        return
    if reaction.emoji.name != "upmartlet" or reaction.message.author == user:
        return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    t = (int(reaction.message.author.id),)
    if not c.execute('SELECT * FROM Members WHERE ID=?', t).fetchall():
        t = (reaction.message.author.id, reaction.message.author.name, 1)
        c.execute('INSERT INTO Members VALUES (?,?,?)', t)
        conn.commit()
        conn.close()
    else:
        c.execute('UPDATE Members SET Upmartlet=Upmartlet+1 WHERE ID=?',t)
        conn.commit()
        conn.close()


@bot.event
@asyncio.coroutine
def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "dammit marty":
        yield from message.channel.send(":c")
    if message.content == "worm":
        yield from message.channel.send("walk without rhythm, and it won't attract the worm.")
    if message.content == "hey":
        yield from message.channel.send("whats going on?")
    yield from bot.process_commands(message)


# Startup extensions
# If statement will only execute if we are running this file (i.e. won't run if its imported)
if __name__ == "__main__":
    for extension in startup:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.run(os.environ.get("DISCORD_TOKEN"))
