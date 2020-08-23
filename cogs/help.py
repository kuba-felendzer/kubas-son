import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

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

    def join_lists(self, list1, list2): 
      
        out = [(list1[i], list2[i]) for i in range(0, len(list1))] 
        return out 

    fullcmdlist = join_lists(commandlist, cmdusagelist)

    @commands.command()
    async def help(self, ctx):
        global commands
        embed = discord.Embed(title="Help", description="retard cant figure it out", color=discord.Color.greyple())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

        for cmd in fullcmdlist:
            embed.add_field(name=cmd[0], value=cmd[1])
    
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))