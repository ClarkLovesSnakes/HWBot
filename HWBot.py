import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix = "")

@bot.event
async def on_message(message):

    yesNo = ["\U00002B06", "\U00002B07"]
    reactions = ["\U0001F603", "\U0001F923", "\U0001F60D", "\U0001F605", "\U0001F61D", "\U0001F644", "\U0001F62C", "\U0001F634", "\U0001F92E", "\U0001F9D0", "\U0001F615", "\U0001F608", "\U0001F47F", "\U0001F4A9", "\U0001F596", "\U0001F918", "\U0001F937", "\U0001F926", "\U0001F171", "\U0001F52B", "\U0001F489", "\U0001F374", "\U0001F4B8", "\U0001F47B", "\U0001F631", "\U0001F980", "\U0000264B", "\U0001F31D", "\U0001F308", "\U0001F595", "\U0001F92F", "\U0001F916", "\U0001F494", "\U0001F346", "\U0001F351", "\U0001F47A", "\U0001F335", "\U0001F3B7", "\U0001F5E1", "\U0001F4A3", "\U000026CF", "\U0001F4E3", "\U0001F4F5", "\U0001F51E", "\U0001F192", "\U0001F195", "\U0001F4AF", "\U0001F476", "\U0001F6D1"]


    verboseReaction = random.randint(1,2) > 1
    if verboseReaction:
        await message.add_reaction(reactions[random.randint(0, (len(reactions) - 1))])
    else:
        await message.add_reaction(yesNo[random.randint(0,1)])


@bot.event
async def on_ready():

    print("Bot is logged in as {0.user}".format(bot))
    print("All systems are online. Awaiting orders.")

@bot.command()
async def quit(ctx):
    
    await ctx.send("Logging Off!")
    await bot.close()
    loop.stop()
    return

async def main():

    # Get the token out of the secret toke doc
    with open("Token.txt", "r", encoding="utf-8") as tokenDoc:
        TOKEN = tokenDoc.readline()


    await bot.start(TOKEN)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
