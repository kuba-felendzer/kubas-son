import discord
from discord.ext import commands
import asyncio

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
        else: await ctx.send("I secksed you're mom :sunglasses:")

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
        await ctx.send(f"OFFICIAL SPEEDRUN OF {arg.upper()} IN 00.23432771 SECONDS!!!!!!!!!!!!!!!!!!!!!")

    @commands.command()
    async def imp(self, ctx):
        await ctx.send(f"who is {ctx.author.name}?\nin math: my solution:currency_exchange:\nin history: my queen:thinking:\nin art: my canvas:art:\nin science: my oxygen:test_tude:\nin geography: my world:world_map:\nin toilet: my shit:poop:)

    @commands.command()
    async def hart(self, ctx):
        for x in range(1, 6):
            await ctx.send(":poop:")
def setup(client):
    client.add_cog(Random(client))