import discord
from discord.ext import commands
global commandlist, cmdusagelist

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.commandlist = ["simp", 
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
                "speedrun",
                "shart",
                "spam",
                "stop",
                "stinky",
                "shotgun",
                "shawty"]
        self.cmdusagelist = ["makes me simp",
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
                "very fast",
                "big poopy",
                "spam `@target` `amount` `message`",
                "stops the spam",
                "ew",
                "for SAS fanboys",
                "2nd best song"]

    @commands.command()
    async def help(self, ctx):
        def join_lists(list1, list2): 
            out = [(list1[i], list2[i]) for i in range(0, len(list1))] 
            return out

        fullcmdlist = join_lists(self.commandlist, self.cmdusagelist)
        embed = discord.Embed(title="Help", description=f"{ctx.author.name} cant figure it out", color=discord.Color.greyple())
        embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)

        for cmd in fullcmdlist:
            embed.add_field(name=cmd[0], value=cmd[1])
    
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))