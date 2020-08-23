import discord
from discord.ext import commands
import asyncio
import random
import os

client = commands.Bot(command_prefix="s")
TOKEN = "NzA2OTQ1MDUzNDE4ODQ4MjU2.XrBn4w.dRJb5w3819bAPjFHbWRPr7s568c"
client.remove_command("help")
global stop, commandlist, cmdusagelist
commandlist = ["simp", 
            "secret tunnel", 
            "sarah palin", 
            "stalin", 
            "sonic", 
            "sip", 
            "scp", 
            "silence", 
            "send feet pics", 
            "sex", 
            "shelp", 
            "shut up", 
            "sing", 
            "snickers", 
            "snort my shit", 
            "speak", 
            "spell icup", 
            "stupid", 
            "succ", 
            "speedrun"]

cmdusagelist = ["makes me simp",
                "my favorite song",
                "she's a hottie",
                "the greatest georgian",
                "he do be zoomin doe",
                "liberal *crunches monster can*",
                "do scp <number>",
                "you cannot.",
                ":flushed::hot_face::hot_face:",
                "sexd mom moment :sunglasses:",
                "this command retar",
                "i will dropkick you",
                "my favorite funny epic dank meme offensive song",
                "you can't say that",
                "do it",
                "i do indeed have vocal cords",
                "no please i don wanna",
                "that's not the word",
                "kono diaaaaaaaaaaaaaaaaaa",
                "very fast"]

def join_lists(list1, list2): 
      
    out = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return out 

fullcmdlist = join_lists(commandlist, cmdusagelist)

@client.event
async def on_message(message):
    if message.channel.name == 'hell-on-earth':
        await client.process_commands(message)

@client.event
async def on_ready():
    print("--------------------------------------")
    print(f"Logged in as {client.user.name}!")
    print("--------------------------------------")

@client.command()
async def help(ctx):
    global commands
    embed = discord.Embed(title="Help", description="retard cant figure it out", color=discord.Color.greyple())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

    for cmd in fullcmdlist:
        embed.add_field(name=cmd[0], value=cmd[1])
    
    await ctx.send(embed=embed)

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            client.load_extension(cog)
        except Exception as e:
            print(f"{cog} cannot be loaded!")
            raise e

client.run(TOKEN)
