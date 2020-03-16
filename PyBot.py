# Either Discord or discord.py uses quotation marks "" to parse arguments.
# This leads to issues when we want to use code such as print("Hello"), as
# now the parser will complain that there isn't a space after the second ".
# To get around this: Use escape characters \, or single quotes '.

# Another way around: Look into keyword-only arguments.

# Update: This was solved using keyword-only arguments.

import discord
from discord.ext import commands

# Define bot description and command prefix.
desc = "Test PyBot"
command_prefix = "!py "

# Make the bot.
pyBot = commands.Bot(command_prefix, description = desc)

# Initialize the bot.
@pyBot.event
async def on_ready():
    print('PyBot is ready.')

# A test function that will return what it was given.
@pyBot.command()
async def debug(context, *, msg):
    print(f"RECIEVED: {msg}")
    await context.send(f"RECIEVED: {msg}")

# Exec command.
@pyBot.command()
async def python3(context, *, msg):
    await context.send("Running...")
    exec(msg)
    await context.send("Done!")

# Give access to the bot.
pyBot.run("token")

