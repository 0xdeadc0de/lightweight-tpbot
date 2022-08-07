
from collections import defaultdict
import discord
import pymongo
from alayina_gider import Cogcu, TurkProgramcilar, Kanal, embed_sohbet, sunucu_uyesi, idler, Rol
from discord.ext.commands import *
from discord.ext.tasks import *
from mangocu import Mangocu
import re

import random

def sans(yuzde):
    """100% verildiginde random.random() hicbir zaman 100u gecemeyeceginden hep true doner"""
    return random.random() < yuzde
first=True
class Ekonomici(Cogcu):
    @Cog.listener()
    async def on_ready(self):
        global first
        if not first: return; first = False
        self.mango = Mangocu()
        self.mesajcilar = defaultdict(lambda: defaultdict(int))
        self.guncelle.start()

    def risitas_coin_ver(self, id: int, adet: int):
        id = str(id)
        self.mango.uyeyi_guncelle(id, {
            "$inc": {"risitas_coin_pending": adet}})

    @Cog.listener()
    @TurkProgramcilar()
    async def on_message(self, msg: discord.Message):
        #msg=await msg.channel.fetch_message(1005461178312564736)
        if msg.author.bot:
            # DISBOARD
            if msg.author.id != 302050872383242240:
                return

            if msg.embeds[0].image.url != "https://disboard.org/images/bot-command-image-bump.png":
                return

            rsc=100
            self.risitas_coin_ver(msg.interaction.user.id, rsc)
            embed=discord.Embed(
                description="```Afferin evlat. Ekselans Risitas seni aşağıdaki ödüllerle kutsadı.```",
            )
            embed.add_field(name="`Risitas Coin (RSC)`", value=f"```{rsc}```")
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_author(name=msg.interaction.user.display_name, icon_url=msg.interaction.user.display_avatar.url)
            embed.set_image(url="https://i.imgur.com/fi3lnEw.png")
            await msg.channel.send(embed=embed)

            return
            
                
        if msg.thread is not None and msg.thread.is_private:
            return

        if sans(min(1, len(msg.content)**2*1e-4)):
            ricardo_coin = 1
            if msg.thread and sans(.5):
                ricardo_coin += 1

            self.mesajcilar[msg.author.id]["ricardo_coin_pending"] += ricardo_coin

        if sans(.5) and re.match(".*:IBO.{0,2}:.*", msg.content):
            self.mesajcilar[msg.author.id]["ibo_coin_pending"] += 1

        if msg.channel.category_id == idler.paylasimlar:
            self.risitas_coin_ver(msg.author.id, 1)
            return

        if msg.channel.id == Kanal.BugunNeYaptim.id:
            self.risitas_coin_ver(msg.author.id, 500)
            return


    @loop(seconds=15)
    async def guncelle(self):
        if len(self.mesajcilar) == 0:
            return
        self.mango.user.bulk_write(
            [pymongo.UpdateOne({"id": str(id)}, {'$inc': pending}, upsert=True) for id, pending in self.mesajcilar.items()] 
        )
        self.mesajcilar = defaultdict(lambda: defaultdict(int))

    async def _bakiye(self, ctx: discord.ApplicationContext, id=None):
        cuzdan = self.mango.uye(id).cuzdan()
        
        uye = sunucu_uyesi(ctx, int(id))
        if uye is None:
            return

        await ctx.send(embed=embed_sohbet(self.bot.user, 
            f"`{uye.display_name}` adlı üyenin hesap dökümü aşağıda belirtilmiştir.",
            ozellikler={"Ricardo (RCC)": cuzdan.ricardo, "Risitas (RSC)": cuzdan.risitas, "İbo (IBO)": cuzdan.ibo},
            resim="https://i.imgur.com/T9rS8qU.png"
        ))


    @command()
    @TurkProgramcilar()
    @Kanal.BotKomutlar.mi()
    @cooldown(1, 15, BucketType.user)
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
    @cooldown(1, 15, BucketType.user)
    async def paraciklar(self, ctx: discord.ApplicationContext):
        """Bekleyen Ricardo (RCC) ve Risitas (RSC) coin'leri toplar"""
        cuzdan = self.mango.uye(ctx.author.id).cuzdan()
        if cuzdan.pending_ricardo ==  cuzdan.pending_risitas == cuzdan.pending_ibo == 0:
            await ctx.send("Bekleyen coin'iniz bulunmamaktadır.")
            return
        
        self.mango.uyeyi_guncelle(ctx.author.id, {
            "$set": {"ricardo_coin_pending": 0, "risitas_coin_pending": 0, "ibo_coin_pending": 0}, 
            "$inc": {"ricardo_coin": cuzdan.pending_ricardo, "risitas_coin": cuzdan.pending_risitas, "ibo_coin": cuzdan.pending_ibo}})
        await ctx.send(embed=embed_sohbet(self.bot.user,
            f"`{ctx.author.display_name}` bekleyen coin'lerini topladı. Kazanımlar:",
            ozellikler={"Ricardo (RCC)": cuzdan.pending_ricardo, "Risitas (RSC)": cuzdan.pending_risitas, "İbo (IBO)": cuzdan.pending_ibo},
            resim="https://c.tenor.com/rD9QG-wudPoAAAAC/cat-cashier.gif"
        ))
        

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            await ctx.send(error)
        else:
            raise error

def main():
    Ekonomici("TPBOT_TOKEN_BAKKAL", Ekonomici.__name__.lower())
if __name__ == "__main__":
    main()