import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with the token you copied from the Discord Developer Portal.
TOKEN = 'YOUR_BOT_TOKEN'
PREFIX = '!'  # You can set your desired bot command prefix here.

# Create a bot instance with a command prefix.
bot = commands.Bot(command_prefix=PREFIX)

# Event to execute when the bot is ready and connected to Discord.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Sample command to test the bot.
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot using the bot token.
bot.run(TOKEN)