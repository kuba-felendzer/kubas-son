import discord
from discord.ext import commands
import asyncio
import random

class Random(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ilence(self, ctx):
        await ctx.send("you cannot suppress me commie fucker")

    @commands.command()
    async def ing(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/657338714850197505/740643115618271302/IMG428707969551654037.mp4")

    @commands.command()
    async def ex(self, ctx, *, arg=""):
        if arg == "funny": await ctx.send("haha sex funi")
        else: await ctx.send(f":face_vomiting: {ctx.author.mention} unironically has sexks before marriage")

    @commands.command()
    async def ecks(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/746906063776907284/769633600995721266/image0.png")

    @commands.command()
    async def tupid(self, ctx):
        await ctx.send("hey the term is \"redditard\" nerd")

    @commands.command()
    async def pell(self, ctx, *, arg):
        if "icup" in arg or "ICUP" in arg:
            await ctx.send("I-C-U-P")
            await asyncio.sleep(1.3)
            await ctx.send("WAIT FUCK")
        else: await ctx.send("no retar\nspell it yourself")

    @commands.command(aliases=["tfu"])
    async def hut(self, ctx, *, arg=""):
        if "bitch" in arg or "up" in arg: await ctx.send("no you shut the fuck up you fat whore.\nyou are not loved nor needed in this server.\ntell me who invited you, so i can ban you both.")

    @commands.command()
    async def peak(self, ctx):
        await ctx.send("no period symbol")
        await asyncio.sleep(45)
        await ctx.send(".")

    @commands.command(aliases=["uck"])
    async def ucc(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send("Yoo IS THAT A MOTHERFUCCIN JOJO REFERENCE?!?!:100::100::o2::o2::100::100::o2::o2::100::no_entry_sign::100::no_entry_sign: ORAORAORAORAORAORA:sunglasses::atm::sunglasses::atm::sunglasses::atm::sunglasses::atm: MUDAMUDAMUDAMUDAMUDAMUDA:fire::hot_face::fire::hot_face::fire::hot_face::fire::hot_face: KILL DA HOE BEEEEEEEETCH:clown::no_entry_sign::clown::sos::clown::sos::clown::sos::no_entry_sign::no_entry_sign::no_entry_sign::b: GIORNO THEME:oncoming_police_car::oncoming_police_car::oncoming_police_car::oncoming_police_car::oncoming_police_car::oncoming_police_car:ZA WARUDO:medal::military_medal::medal::military_medal::medal::military_medal::medal::military_medal: AYAYAYAYYYYYYYY :scream::scream::scream::scream::scream::scream::scream::face_with_symbols_over_mouth: Yo Angelo! Yo Angelo! Yo Angelo! Yo Angelo! Yo Angelo! Yo Angelo!:moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai::moyai: I WANT TRISH AND JOLYNE HENTAI:tokyo_tower::statue_of_liberty::tokyo_tower::statue_of_liberty::tokyo_tower::statue_of_liberty::tokyo_tower::statue_of_liberty: PUCCI PLEASE RESET THE WORLD BECAUSE ARAKI FORGOT:beach_umbrella::beach_umbrella::beach_umbrella::beach_umbrella::beach_umbrella::beach_umbrella::beach_umbrella: KONO DIO DAAAAAA! RODO ROLA DAA!!!!:tickets::tickets::tickets::tickets::tickets::tickets::clapper: THE END.")

    @commands.command()
    async def nort(self, ctx, *, arg):
        if "my shit" in arg:
            await ctx.send(":flushed:")

    @commands.command()
    async def nickers(self, ctx):
        await ctx.send("ok white bitch")

    @commands.command()
    async def kyrim(self, ctx):
        await ctx.send("i want to fuck todd howard.")

    @commands.command()
    async def piderman(self, ctx):
        await ctx.send("tom holland? more like chopped up into pieces and shoved into my freezer :sunglasses::hot_face:")

    @commands.command()
    async def team(self, ctx):
        for x in range(0, 69):
            await ctx.send("hail GabeN")
            await asyncio.sleep(1)

    @commands.command()
    async def ip(self, ctx):
        await asyncio.sleep(.7)
        await ctx.send("*cracks open monster can*")
        await asyncio.sleep(1.2)
        await ctx.send("*slurp*")
        await asyncio.sleep(.7)
        await ctx.send("liberal")

    @commands.command()
    async def arah(self, ctx, *, arg):
        if arg == "palin": await ctx.send("ok libtard, just because i jack off to sarah palin hentai doesnt make me a degenerate, it makes a red-blooded american man!")

    @commands.command()
    async def talin(self, ctx):
        await ctx.send("stalin was from the sweet of georgia, so guess what, **liberal**, the man who defeated fascism was a confederate!")

    @commands.command()
    async def onic(self, ctx):
        await ctx.send("NNNNYYYYYYYYYOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMM")

    @commands.command()
    async def ecret(self, ctx, *, arg):
        if arg == "tunnel": await ctx.send("urethra moment")

    @commands.command()
    async def peedrun(self, ctx, *, arg):
        await ctx.send(f"OFFICIAL SPEEDRUN OF {arg.upper()} IN 00.{random.randint(10000, 99999)} SECONDS!!!!!!!!!!!!!!!!!!!!!")

    @commands.command()
    async def imp(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(1.3)
        await ctx.send(f"who is {ctx.author.name}?\nin math: my solution:currency_exchange:\nin history: my queen:thinking:\nin art: my canvas:art:\nin science: my oxygen:test_tube:\nin geography: my world:world_map:\nin toilet: my shit:poop:")

    @commands.command(aliases=["hit"])
    async def hart(self, ctx):
        if ctx.author.id == "noofio#5180": await ctx.send("no mr. shit spammer")
        else:
            for x in range(1, 6):
                await ctx.send(":poop:")

    @commands.command(aliases=["melly"])
    async def tinky(self, ctx):
        await ctx.send(f"god damn you smell, {ctx.author.name}")

    @commands.command()
    async def hotgun(self, ctx):
        await ctx.send("Mossberg 590A1 meta in Tom Clancy's Rainbow Six Siege")

    @commands.command(aliases=["hawty"])
    async def horty(self, ctx):
        lyrics = [
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "Remember the first time we met\nYou was at the mall with your friends\nI was scared to approach ya\nBut then you came closer\nHopin' you would give me a chance",
            "Who would have ever knew\nThat we would ever be more than friends\nWe're real worldwide, breakin all the rules\nShe like a song played again and again",
            "That girl, like somethin off a poster\nThat girl, is a dime they say\nThat girl, is a gun to my holster\nShe's runnin through my mind all day, ay",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "See you been all around the globe\nNot once did you leave my mind\nWe talk on the phone, from night til the morn\nGirl you really change my life\nDoin things I never do\nI'm in the kitchen cookin things she likes",
            "We're real worldwide, breakin all the rules\nSomeday I wanna make you my wife\nThat girl, like somethin off a poster\nThat girl, is a dime they say\nThat girl, is the gun to my holster\nShe's runnin through my mind all day, ay",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "I can be your melody\nA girl that could write you a symphony\nThe one that could fill your fantasies\nSo come baby girl let's sing with me\nAy, I can be your melody\nA girl that could write you a symphony\nThe one that could fill your fantasies\nSo come baby girl let's sing with me",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay",
            "Shawty's like a melody in my head\nThat I can't keep out\nGot me singin' like\nNa na na na everyday\nIt's like my ipod stuck on replay, replay-ay-ay-ay"
        ]
        for line in lyrics:
            await ctx.send(line)
            await asyncio.sleep(3)
    
    @commands.command()
    async def weat(self, ctx): await ctx.send("<@458415107651665942>")

    @commands.command()
    async def ad(self, ctx): await ctx.send("so there was this cake competition right")

def setup(client):
    client.add_cog(Random(client))