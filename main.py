import os
import random
import discord

from tools import Message
from tools import Emoji
from discord.ext import commands


bot = commands.Bot(command_prefix='$')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def help(ctx):
    await ctx.send("""
        Команды:
          `$vk_sticker [N]` рандомный стикер из vk (либо конкретный с номером N из [1, 10451])
    """)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    emojies = Emoji.get_from_message(message)

    id = Message.insert(message)

    if emojies:
        Message.insert_emojies(id, emojies)

    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(os.environ['BOT_TOKEN'])
