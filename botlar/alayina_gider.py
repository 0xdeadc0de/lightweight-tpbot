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
import asyncio

cogbotlar = {}
class Cogcu(Cog):
    def __init__(self, token_ismi, cog_ismi):
        self.token_ismi = token_ismi
        self.cog_ismi = cog_ismi
        # ekle
        global cogbotlar
        rutin = None
        if token_ismi not in cogbotlar.keys():
            cogbot = Tpbot(self.token_ismi)
            cogbotlar[token_ismi] = cogbot
            rutin = cogbot.baslat(self)
            cogbot.gunluk("bot baslatildi ve cogcu eklendi =>", self.cog_ismi)
        else:
            cogbot = cogbotlar[token_ismi]
            rutin = cogbot.add_cog(self)
            cogbot.gunluk("varolan bota cogcu eklendi =>", self.cog_ismi)

        try:
            asyncio.get_running_loop()
            asyncio.create_task(rutin)
        except:
            asyncio.run(rutin)

class TemelKomutlar(Cog):
    def __init__(self, token_ismi):
        self.token_ismi = token_ismi

    @command()
    @check(yonetici_mi)
    async def ping(self, ctx):
        await ctx.send(f'pong [{self.token_ismi}]')

    @command()
    @check(yonetici_mi)
    async def kapan(self, ctx, hedef):
        if hedef == self.token_ismi:
            react = self.bot.get_emoji(837392046725136424) # RISITAS HANDWAVE
            if react is None:
                react = '\N{Waving Hand Sign}'
            await ctx.message.add_reaction(react)
            exit(1)

class Tpbot(Bot):
    cogs = []
    def __init__(self, token_ismi) -> None:
        self.cogs.append(TemelKomutlar(token_ismi))
        self.token_ismi = token_ismi
        self.gunluk("merhaba dünya!")
        super().__init__(command_prefix="$", intents=discord.Intents.all())

    async def baslat(self, cogcu=None):
        if cogcu:
            self.cogs.append(cogcu)
        for cog in self.cogs:
            await self.add_cog(cog)
        token = os.environ.get(self.token_ismi)
        if token is None:
            self.gunluk(f"{self.token_ismi} degeri tanimli degil")
            exit(-1)
        await self.start(token)

    def gunluk(self, *mesajlar):
        print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{self.token_ismi}]:", *mesajlar)

    async def on_ready(self):
        self.gunluk("atis serbest", self.user)