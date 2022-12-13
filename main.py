import discord
from discord.ext import commands
import asyncio

f = open("TOKEN", "r")
token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Bot Ready!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def test(ctx):
    await ctx.send("Okay!")

bot.run(token)

# test comment to test github + vscode functionality