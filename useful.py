import discord
from discord.ext import commands
import asyncio

class Useful(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pamist(self, ctx, *, arg):
        badwords = ["bad", "stinky", "sucks", "smelly", "retar", "retarded", "retarred", "dummy"]
        if arg in badwords:
            await ctx.send("you've fucked up, buddy retard.")
            await asyncio.sleep(1)
            await ctx.send("prepare to get nannered")
            await asyncio.sleep(1)
            looplist = [5, 4, 3, 2, 1]
            for item in looplist:
                if item <= 2: await ctx.send(f"**{item}**")
                else: await ctx.send(f"{item}")
                await asyncio.sleep(1)

            await ctx.send(":banana:")
            await asyncio.sleep(.8)
            hours = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            for hour in hours:
                if hour != 1: await ctx.send(f"{ctx.author.mention}, {hour} hours.")
                else: await ctx.send(f"{ctx.author.mention}, {hour} hour.")
                await asyncio.sleep(3600)

            await ctx.send("and now, they are coming.")

        elif arg == "good":
            await ctx.send("i would give you mod but granddaddy daniel said no")

    @commands.command()
    async def end(self, ctx, *, arg):
        if "feet pics" in arg:
            await ctx.send("ok retard\nhttps://www.wikifeet.com/Imane_%27Pokimane%27_Anys")

    @commands.command()
    async def cp(self, ctx, id = "", literal=""):
        allowedLiterals = ["l", "lit", "literal", "ltl"]
        if literal in allowedLiterals: newID = id
        else:
            if len(id) == 1: newID = f"00{id}"
            elif len(id) == 2: newID = f"0{id}"
            else: newID = id

        if newID == "":
            await ctx.send("how fucking stupid are you, cant even pick one. try 999 nerd\nhttp://www.scpwiki.com/scp-999")
        else:
            await ctx.send(f"http://www.scpwiki.com/scp-{newID}")

def setup(client):
    client.add_cog(Useful(client))