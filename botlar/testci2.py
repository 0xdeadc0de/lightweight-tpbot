from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class Testci2(Cogcu):
    @command()
    @check(yonetici_mi)
    async def ping2(self, ctx):
        await ctx.send(f'pong2 [{self.token_ismi}]')

Testci2("TPBOT_TOKEN_TEST", Testci2.__name__.lower())