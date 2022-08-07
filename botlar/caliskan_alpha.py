from pydoc import describe
import discord
from alayina_gider import Cogcu, idler
from discord.commands import *

class Caliskan(Cogcu):
    @slash_command(guild_ids=[idler.sunucu], description="kod parçası çalıştırır")
    @option("dil", description="hangi dil? örn: python, py, javascript, js...")
    @option("kod", description="çalıştırılacak kod")
    async def caliskanim(self, ctx: discord.ApplicationContext, dil: str, kod: str):
        await ctx.respond("Hi, this is a slash command from a cog!", ephemeral=True)

Caliskan("TPBOT_TOKEN_TEST", Caliskan.__name__.lower())