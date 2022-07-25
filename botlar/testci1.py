from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class testci1(Cogcu):
    @command()
    @check(yonetici_mi)
    async def ping1(self, ctx):
        await ctx.send(f'pong1 [{self.token_ismi}]')

testci1("TPBOT_TOKEN_TEST", testci1.__name__)