from alayina_gider import Tpbot, yonetici_mi
from discord.ext.commands import *

bot = Tpbot("TPBOT_TOKEN_TEST")

@bot.command()
@check(yonetici_mi)
async def testkapat(ctx):
    exit(1)

bot.baslat()