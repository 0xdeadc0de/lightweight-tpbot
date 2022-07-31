from enum import Enum
from discord.ext.commands import *
import discord
import time
import os
import asyncio

class idler:
    yoneticiler = [
        824573651390562325, # Kral Risitas
        272044185689915392, # MrChuck
    ]
    sunucu = 698972054740795453
def yonetici_mi(ctx):
    return ctx.author.id in idler.yoneticiler

class TDK:
    def miYapici(sorgu):
        def mi(id):
            async def kontrol(ctx):
                return sorgu(ctx) == id
            return lambda: check(kontrol)
        return mi

    def varMiYapici(sorgu):
        def mi(id):
            async def kontrol(ctx):
                return id in sorgu(ctx)
            return lambda: check(kontrol)
        return mi


class Kanal:
    mi = TDK.miYapici(lambda ctx: ctx.channel.id)
class Kanal:
    class TpbotTest1:
        id = 803590557355474964
        mi = Kanal.mi(id)
    class TpbotTest2:
        id = 824378307008790612
        mi = Kanal.mi(id)
    class TpbotKomutlar:
        id = 852552268430966824
        mi = Kanal.mi(id)
    class MerhabaDunya:
        id = 900650376762626078
        mi = Kanal.mi(id)
    class SoruSor:
        id = 1003249327117979739
        mi = Kanal.mi(id)


class Yonetici:
    mi = TDK.miYapici(lambda ctx: ctx.author.id)
class Yonetici:
    class KralRisitas:
        id = 824573651390562325
        mi = Yonetici.mi(id)
    class MrChuck:
        id = 272044185689915392
        mi = Yonetici.mi(id)


class Rol:
    varMi = TDK.varMiYapici(lambda ctx: ctx.author.roles)
class Rol:
    class Asistan:
        id = 826741535839748096
        varMi = Rol.varMi(id)
    class Editor:
        id = 830478022183616564
        VarMi = Rol.varMi(id)
    class Kurucu:
        id = 801135743229624320
        VarMi = Rol.varMi(id)

        
    def AsistanEditorKurucuMu():
        async def kontrol(ctx):
            return any(rol.id in [Rol.Asistan.id,Rol.Editor.id,Rol.Kurucu.id] for rol in ctx.author.roles)
        return check(kontrol)


async def thumbs(ctx, condition):
    if condition:
        await thumbs_up(ctx)
    else:
        await thumbs_down(ctx)
async def thumbs_up(ctx):
    await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
async def thumbs_down(ctx):
    await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')

async def wave(bot, ctx):
    react = bot.get_emoji(837392046725136424) # RISITAS HANDWAVE
    if react is None:
        react = '\N{Waving Hand Sign}'
    await ctx.message.add_reaction(react)

class TemelKomutlar(Cog):
    def __init__(self, token_ismi, bot):
        self.token_ismi = token_ismi
        self.bot = bot

    @command()
    @check(yonetici_mi)
    async def echo(self, ctx, echo):
        await ctx.send(echo)

    @command()
    @check(yonetici_mi)
    async def ping(self, ctx):
        await ctx.send(f'pong [{self.token_ismi}]')

    @command(aliases=["kapat"]) 
    @check(yonetici_mi)
    async def kapan(self, ctx, hedef):
        if self.bot.get_cog(hedef.capitalize()) is not None or \
           self.bot.get_cog(hedef.lower()) is not None:

            result = self.bot.remove_cog(hedef.capitalize()) or \
                self.bot.remove_cog(hedef.lower())

            await thumbs(ctx, result is not None)


class Tpbot(Bot):
    cogs = []
    def __init__(self, token_ismi) -> None:
        self.cogs.append(TemelKomutlar(token_ismi, self))
        self.token_ismi = token_ismi
        self.gunluk("merhaba dünya!")
        super().__init__(command_prefix="!" if os.environ.get("TPBOT_DEBUG") is None else "$", intents=discord.Intents.all())

    async def baslat(self, cogcu=None):
        if cogcu:
            self.cogs.append(cogcu)
        for cog in self.cogs:
            self.add_cog(cog)
        token = os.environ.get(self.token_ismi)
        if token is None:
            self.gunluk(f"{self.token_ismi} degeri tanimli degil")
            exit(-1)
        await self.start(token)

    def gunluk(self, *mesajlar):
        print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{self.token_ismi}]:", *mesajlar)

    async def on_ready(self):
        self.gunluk("atis serbest", self.user)

        
cogbotlar : dict[str, Tpbot] = {}
class Cogcu(Cog):
    def __init__(self, token_ismi, cog_ismi):
        self.token_ismi = token_ismi
        self.cog_ismi = cog_ismi
        
        global cogbotlar
        rutin = None
        if token_ismi not in cogbotlar.keys():
            cogbot = Tpbot(self.token_ismi)
            cogbotlar[token_ismi] = cogbot
            # fork and add process to cogbotlar
            rutin = cogbot.baslat(self)
            cogbot.gunluk("bot baslatildi ve cogcu eklendi =>", self.cog_ismi)
        else:
            cogbot = cogbotlar[token_ismi]
            if cogbot.get_cog(cog_ismi) is None:
                cogbot.add_cog(self)
                cogbot.gunluk("varolan bota cogcu eklendi =>", self.cog_ismi)
                return
            else:
                cogbot.gunluk("cogcu zaten yuklu =>", self.cog_ismi)
                return

        self.bot = cogbot

        try:
            asyncio.get_running_loop()
            asyncio.create_task(rutin)
        except:
            asyncio.run(rutin)