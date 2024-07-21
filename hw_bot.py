import pathlib
import discord
from discord.ext import commands
import asyncio
import random
import logging

intents = discord.Intents.default()
intents.reactions = True
bot = commands.Bot(intents=intents, command_prefix="")


@bot.event
async def on_message(msg):
    arrow_list = ["⬆️", "⬇️"]

    reactions_path = pathlib.Path(__file__).parent / "reactions.txt"
    with open(reactions_path, "r", encoding="utf-8") as rf:
        reactions_list = rf.readlines()

    if random.randint(0, 1) > 0:
        await msg.add_reaction(random.choice(reactions_list).strip())
    else:
        await msg.add_reaction(random.choice(arrow_list))


async def main():
    discord.utils.setup_logging(leve=logging.INFO, root=False)

    # get the token out of the secret toke doc
    with open("Token.txt", "r", encoding="utf-8") as fp:
        token = fp.read()

    async with bot:
        await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
