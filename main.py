import discord
from discord.ext import commands
import asyncio
import random
import os

TOKEN = open("token.txt", "r").read()
client = commands.Bot(command_prefix="s")
for line in open("token.txt"): TOKEN = line
client.remove_command("help")
global stop, commandlist, cmdusagelist

@client.event
async def on_message(message):
    if message.channel.name in ["hell-on-earth", "speacial-containment-protocal"]:
        await client.process_commands(message)

@client.event
async def on_ready():
    print("--------------------------------------")
    print(f"Logged in as {client.user.name}!")
    print("--------------------------------------")

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            client.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded!")
            raise e

client.run(TOKEN)
