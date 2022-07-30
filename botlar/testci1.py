from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class Testci1(Cogcu):
    @command()
    @check(yonetici_mi)
    async def ping1(self, ctx):
        await ctx.send(f'pong1 [{self.token_ismi}]')

Testci1("TPBOT_TOKEN_TEST", Testci1.__name__.lower())