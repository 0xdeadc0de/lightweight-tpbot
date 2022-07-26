import discord
from alayina_gider import Cogcu, yonetici_mi, Yonetici, Kanal
from discord.ext.commands import *

class Testci1(Cogcu):
    @command()
    @check(yonetici_mi)
    async def ping1(self, ctx):
        await ctx.send(f'pong1 [{self.token_ismi}]')

    @command()
    @Yonetici.KralRisitas.mi()
    async def kralping(self, ctx):
        #uye = ctx.author
        #for x in uye.guild.roles:
        #    if "Bilen" in x.name:
        #        await x.edit(name=x.name[:-6])
        
        await ctx.send(f'kral pong')

    @command()
    @Yonetici.MrChuck.mi()
    async def chuckping(self, ctx):
        await ctx.send(f'chuck pong')

    @slash_command()
    @cooldown(1, 15, BucketType.user)
    @Kanal.TpbotTest1.mi()
    async def test(self, ctx: discord.ApplicationContext, uye: discord.Member):
        await ctx.respond("sadece tpbottest1 kanalinda calisir secilen uye:"+uye.display_name)

def main():
    Testci1("TPBOT_TOKEN_TEST", Testci1.__name__.lower())
if __name__ == "__main__":
    main()