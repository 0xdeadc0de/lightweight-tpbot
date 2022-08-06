
from collections import defaultdict
import discord
import pymongo
from alayina_gider import Cogcu, TurkProgramcilar, Kanal, Rol, sunucu_uyesi, idler
from discord.ext.commands import *
from discord.ext.tasks import *
from mangocu import Mangocu
from copy import copy

import random

def sans(yuzde):
    """100% verildiginde random.random() hicbir zaman 100u gecemeyeceginden hep true doner"""
    return random.random() < yuzde

class Ekonomici(Cogcu):
    @Cog.listener()
    async def on_ready(self):
        self.mango = Mangocu()
        self.mesajcilar = defaultdict(int)
        self.guncelle.start()

    def risitas_coin_ver(self, id: int, adet: int):
        id = str(id)
        self.mango.uyeyi_guncelle(id, {
            "$inc": {"risitas_coin_pending": adet}})

    @Cog.listener()
    @TurkProgramcilar()
    async def on_message(self, msg: discord.Message):
        if msg.author.bot:
            # DISBOARD
            if msg.author.id != 302050872383242240:
                return

            if msg.embeds[0].title != 'DISBOARD: Sunucu Listesi':
                return

            rsc=100
            self.risitas_coin_ver(msg.interaction.user.id, rsc)
            embed=discord.Embed(
                description="```Afferin evlat. Ekselans Risitas seni aşağıdaki ödüllerle kutsadı.```",
            )
            embed.add_field(name="`Risitas Coin (RSC)`", value=f"```{rsc}```")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_author(name=msg.interaction.user.display_name, icon_url=msg.interaction.user.display_avatar.url)
            await msg.channel.send(embed=embed)

            return
            
                
        if msg.thread is not None and msg.thread.is_private:
            return

        if sans(min(1, len(msg.content)**2*1e-4)):
            ricardo_coin = 1
            if msg.thread and sans(.5):
                ricardo_coin += 1

            self.mesajcilar[msg.author.id] += ricardo_coin

        if msg.channel.category_id == idler.paylasimlar:
            self.risitas_coin_ver(1)
            return


    @loop(minutes=1)
    async def guncelle(self):
        if len(self.mesajcilar) == 0:
            return
        kopya = copy(self.mesajcilar)
        self.mesajcilar = defaultdict(int)
        self.mango.user.bulk_write(
            [pymongo.UpdateOne({"id": str(id)}, {'$inc': {"ricardo_coin_pending": coin}}, upsert=True) for id, coin in kopya.items()] 
        )

    async def _bakiye(self, ctx: discord.ApplicationContext, id=None):
        kullanici = self.mango.uyeyi_bul(id)
        ricardo = 0
        risitas = 0
        if kullanici is not None:
            ricardo = kullanici.get("ricardo_coin") or 0
            risitas = kullanici.get("risitas_coin") or 0
        
        uye = sunucu_uyesi(ctx, int(id))
        if uye is None:
            return

        await ctx.send(f"`{uye.display_name} {ricardo} Ricardo (RCC) ve {risitas} Risitas (RSC) coin'i bulunmaktadır.`")


    @command()
    @TurkProgramcilar()
    @Kanal.BotKomutlar.mi()
    @cooldown(1, 60, BucketType.user)
    async def bakiye(self, ctx):
        """sahip olunan Ricardo (RCC) ve Risitas (RSC) coin'leri gösterir"""
        await self._bakiye(ctx, ctx.message.author.id)
    
    @command()
    @TurkProgramcilar()
    @Rol.AsistanEditorKurucuMu()
    async def bakiyesi(self, ctx: Context, id: str):
        if id.isnumeric() == False:
            if ctx.message.mentions.__len__() == 0:
                return
            id = ctx.message.mentions[0].id
        await self._bakiye(ctx, id)


    @command()
    @TurkProgramcilar()
    @Kanal.BotKomutlar.mi()
    @cooldown(1, 60, BucketType.user)
    async def paraciklar(self, ctx: discord.ApplicationContext):
        """Bekleye Ricardo (RCC) ve Risitas (RSC) coin'leri toplar"""
        kullanici = self.mango.uyeyi_bul(ctx.author.id)
        ricardo = 0
        risitas = 0
        if kullanici is not None:
            ricardo = kullanici.get("ricardo_coin_pending") or 0
            risitas = kullanici.get("risitas_coin_pending") or 0
        if kullanici is None or ricardo == risitas == 0:
            await ctx.send("Bekleyen coin'iniz bulunmamaktadır.")
            return
        
        self.mango.uyeyi_guncelle(ctx.author.id, {
            "$set": {"ricardo_coin_pending": 0, "risitas_coin_pending": 0}, 
            "$inc": {"ricardo_coin": ricardo, "risitas_coin": risitas}})
        await ctx.send(f"`{ctx.author.display_name} bekleyen {ricardo} Ricardo (RCC) ve {risitas} Risitas (RSC) coin'lerini topladı.`")
        

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            await ctx.send(error)
        else:
            raise error

Ekonomici("TPBOT_TOKEN_BAKKAL", Ekonomici.__name__.lower())