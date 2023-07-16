import pathlib
import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix="")

@bot.event
async def on_message(message):

    arrow_list = ["⬆️", "⬇️"]

    reactions_path = pathlib.Path(__file__).parent / "reactions.txt"
    with open(reactions_path, "r", encoding="utf-8") as rf:
        reactions_list = rf.readlines()

    if random.randint(0, 1) > 0:
        await message.add_reaction(random.choice(reactions_list))
    else:
        await message.add_reaction(random.choice(arrow_list))


async def main():

    # get the token out of the secret toke doc
    token_path = pathlib.Path(__file__).parent / "token.secret"
    with open(token_path, "r", encoding="utf-8") as tf:
        token = tf.readline()

    await bot.start(token)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
