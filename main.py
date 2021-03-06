import os
import random
import discord

from tools import Message
from tools import Emoji
from tools import Statistic
from tools import Joker

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
          `$show_stat` статистика использования смайликов)
    """)


@bot.command()
async def vk_sticker(ctx, id=0):
    if not id:
        id = random.randint(1, 10451)

    await ctx.message.delete()

    embed = discord.Embed()
    embed.set_image(url='https://vk.com/images/stickers/' + str(id) + '/512.png')

    await ctx.send("Стикер отослан: %s" % ctx.message.author, embed=embed)


@bot.command()
async def show_stat(ctx):
    rows = Statistic.smile_count(ctx.message.channel.id)
    owned_emojies = ctx.message.guild.emojis
    smiles_to_print = []
    template = "<:%s:%s> — %s"

    for emoji in owned_emojies:

        for row in rows:
            if row[1] == str(emoji.id):
                smiles_to_print.append(row)

    sorted_smiles = sorted(smiles_to_print, key=lambda x: x[2], reverse=True)
    smiles = list(map(lambda emoji: template % emoji, sorted_smiles))
    header = "Статистика использования кастомных смайлов: \n"
    message = "Информации нет ¯\_(ツ)_/¯"
    if len(smiles) != 0:
        message = header + "\n".join(smiles)

    await ctx.send(message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    emojies = Emoji.get_from_message(message)

    id = Message.insert(message)

    if emojies:
        Message.insert_emojies(id, emojies)

    if Joker.wants_joke(message.content):
        await Joker.joke(message.channel)

    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(os.environ['BOT_TOKEN'])
