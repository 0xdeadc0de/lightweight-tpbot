from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class testci2(Cogcu):
    @command()
    @check(yonetici_mi)
    async def ping2(self, ctx):
        await ctx.send(f'pong2 [{self.token_ismi}]')

testci2("TPBOT_TOKEN_TEST", testci2.__name__)