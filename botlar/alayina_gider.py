class idler:
    yoneticiler = [
        824573651390562325, # Kral Risitas
        272044185689915392, # MrChuck
    ]
    sunucu = 698972054740795453
def yonetici_mi(ctx):
    return ctx.author.id in idler.yoneticiler

from discord.ext.commands import *
import discord
import time
import os
import asyncio

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