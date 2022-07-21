yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
def yonetici_mi(ctx):
    return ctx.author.id in yoneticiler

from discord.ext.commands import *
import discord
import time
import os

class TemelKomutlar(Cog):
    def __init__(self, bot, token_ismi):
        self.token_ismi = token_ismi
        self.bot = bot

    @command()
    @check(yonetici_mi)
    async def ping(self, ctx):
        await ctx.send(f'pong [{self.token_ismi}]')

    @command()
    @check(yonetici_mi)
    async def kapan(self, ctx, hedef):
        if hedef == self.token_ismi:
            react = self.bot.get_emoji(837392046725136424) # RISITAS
            if react is None:
                react = '\N{Waving Hand Sign}'
            await ctx.message.add_reaction(react)
            exit(1)

class Tpbot(Bot):
    def __init__(self, token_ismi) -> None:
        self.token_ismi = token_ismi
        self.gunluk("merhaba dünya! dosyamin ismi: ", __file__)
        super().__init__(command_prefix="$", intents=discord.Intents.all())

    def baslat(self):
        token = os.environ.get(self.token_ismi)
        if token is None:
            self.gunluk(f"{self.token_ismi} degeri tanimli degil")
            exit(-1)
        self.run(token)

    def gunluk(self, *mesajlar):
        print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{self.token_ismi}]:", *mesajlar)

    async def on_ready(self):
        await self.add_cog(TemelKomutlar(self, self.token_ismi))
        self.gunluk("atis serbest", self.user)