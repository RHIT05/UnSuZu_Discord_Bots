# bot.py
import os
import subprocess
import uuid

import cached_property
import discord
import segno
from discord.ext import commands

TOKEN = os.environ["DISCORD_BOT2_TOKEN"]


async def debug(thing):
    for key in dir(thing):
        if key.startswith("_"):
            continue
        attr = getattr(thing, key)
        print(f"{thing.__class__.__name__}.{key}: {attr}")


def what(*args, **kwargs):
    for i, arg in enumerate(args):
        print(f"{i}: {arg}")
    for key, arg in kwargs.items():
        print(f"{key}: {arg}")


from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Logged on as", bot.user)


@bot.command()
async def ping(ctx):
    await debug(ctx)
    await ctx.send("pong")


@bot.command()
async def qr4(ctx, *args, **kwargs):
    await debug(ctx)
    what(*args, **kwargs)

    text = "".join(args)
    qr = segno.make(text)
    qr.save("/tmp/test.png")
    await ctx.send("/tmp/test.png")


import io


@bot.command()
async def embed_test(ctx, *args):
    qr = segno.make("Hello World")
    qr.save("qr_small.png")
    qr.save("qr_big.png", scale=10)
    embed = discord.Embed(description="Description")

    await ctx.send(embed=embed)


@bot.command()
async def twofa(ctx, *args):
    text = uuid.uuid4()
    qr = segno.make("Hello World")
    qr.save("qr_small.png")
    qr.save("qr_big.png", scale=10)
    embed = discord.Embed(description="Description")

    await ctx.send(embed=embed)


import io


@bot.command()
async def doge(ctx, *args):
    await debug(ctx.author)
    text = "".join(args)
    qr = segno.make("".join(args))
    qr.save("/tmp/qr_big.png", scale=10)
    with open("dogecoin.txt", "a") as myfile:
        myfile.write(f"{ctx.author}: {text}")
        await ctx.send(f"Recorded DogeCoin address for {ctx.author}")

    await ctx.send(file=discord.File("/tmp/qr_big.png", filename="test.png"))


if __name__ == "__main__":
    bot.run(TOKEN)
