from enum import Enum
from discord.ext.commands import *
import discord
import time
import os
import asyncio

def cevap(ctx):
    if type(ctx) is discord.interactions.Interaction:
        return ctx.response.send_message
    else:
        return ctx.respond

def sunucu_uyesi(ctx: discord.ApplicationContext, id: int) -> None | discord.Member:
    if ctx.guild is None:
        return None
    return discord.utils.get(ctx.guild.members, id=id)

def interaction_member(interaction: discord.Interaction) -> None | discord.Member:
    if interaction.guild is None:
        return None
    return discord.utils.get(interaction.guild.members, id=interaction.user.id)

class idler:
    yoneticiler = [
        824573651390562325, # Kral Risitas
        272044185689915392, # MrChuck
    ]
    sunucu = 698972054740795453
    paylasimlar = 832158366541283358
def yonetici_mi(ctx):
    return ctx.author.id in idler.yoneticiler

def TurkProgramcilar():
    async def kontrol(ctx):
        return ctx.guild.id == idler.sunucu
    return check(kontrol)

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
    class BotKomutlar:
        id = 841987730551603200
        mi = Kanal.mi(id)
    class BugunNeYaptim:
        id = 867492591825190932
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

def gunluk(token_ismi, *mesajlar):
    print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{token_ismi}]:", *mesajlar)

def ortamaBirBak(isim):
    deger = os.environ.get(isim)
    if deger is None:
        gunluk(isim, f"{isim} degeri tanimli degil")
        exit(-1)
    return deger

def HEROKU():
    return os.environ.get("TPBOT_DEBUG") is None
def DEBUG():
    return not HEROKU()

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
        super().__init__(command_prefix="!" if HEROKU() else "$", intents=discord.Intents.all())

    async def baslat(self, cogcu=None):
        if cogcu:
            self.cogs.append(cogcu)
        for cog in self.cogs:
            if self.get_cog(cog.qualified_name) is None:
                self.add_cog(cog)
        token = ortamaBirBak(self.token_ismi)
        await self.start(token)

    def gunluk(self, *mesajlar):
        gunluk(self.token_ismi, *mesajlar)

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
            self.bot = cogbot
            cogbotlar[token_ismi] = cogbot
            # fork and add process to cogbotlar
            cogbot.gunluk("bot baslatildi ve cogcu eklendi =>", self.cog_ismi)
            rutin = cogbot.baslat(self)
            try:
                asyncio.get_running_loop()
                asyncio.create_task(rutin)
            except:
                asyncio.run(rutin)
        else:
            cogbot = cogbotlar[token_ismi]
            self.bot = cogbot
            if cogbot.get_cog(cog_ismi) is None:
                cogbot.add_cog(self)
                cogbot.gunluk("varolan bota cogcu eklendi =>", self.cog_ismi)
                return
            else:
                cogbot.gunluk("cogcu zaten yuklu =>", self.cog_ismi)
                return

import datetime
class Arayuzcu(Cogcu):
    @Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(idler.sunucu)
        if guild is None:
            return
        
        id=self.kanal_id if HEROKU() else Kanal.TpbotTest1.id
        channel = await guild.fetch_channel(id)
        if channel is None:
            return

        async for msg in channel.history(limit=10):
            if msg is not None and msg.author.id == self.bot.user.id:
                await msg.delete()

        await channel.send(content=self.baslik+(f" `{datetime.datetime.now()}`" if DEBUG() else ""), embeds=self.embedler(), view=self.Arayuz(bot=self.bot))