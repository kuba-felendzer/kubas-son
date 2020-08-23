import discord
from discord.ext import commands
import asyncio

class Spam(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.spamming = False

    @commands.command()
    async def pam(self, ctx, target: discord.Member, amount: int, *, message):
        self.spamming = True
        if self.spamming == True:
            for a in range(0, amount):
                if self.spamming:
                    await ctx.send(f"{target.mention}! {message}")
                    await asyncio.sleep(1)
                else: continue

    @commands.command()
    async def top(self, ctx):
        if self.spamming == True: self.spamming = False
        else: await ctx.send("bruh im not spamming")

def setup(client):
    client.add_cog(Spam(client))