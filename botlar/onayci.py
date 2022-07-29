izinli_roller = [
    801135743229624320, #KURUCU
    830478022183616564, #EDITOR
    826741535839748096, #ASISTAN
]
def izinli_rollu_mu(ctx):
    return any(rol.id in izinli_roller for rol in ctx.author.roles)

padisah_fermani = """Merhaba hoş geldiniz. Sizlere bir kaç sorumuz olacak. Lütfen sırayla cevaplayınız.

1->Sunucuyu nereden(kimden,nasıl,disboard vb..) buldunuz ?

2->Gelme amacınız nedir?

3->Programlama ile ilgileniyor musunuz?

4->Neleri biliyorsunuz?

5->Son aldığınız eğitim lise, üniv v.b (opsiyonel olarak yaş ekleyebilirsiniz)?

Cevaplarınızı verdikten sonra, cevaplarınızda bir eksik yok ise kaydınız en kısa sürede onaylanacaktır. Bir eksik çıktığı taktirde sizinle bu sayfa üzerinden iletişime geçilecek ve eksiklerinizi düzeltmeniz istenecektir. İyi kodlar dileriz. 
-TP Yönetim"""

import discord
from alayina_gider import Cogcu
from discord.ext.commands import *

from botlar.alayina_gider import thumbs_down, thumbs_up

class Onayci(Cogcu): 
    @command()
    @check(izinli_rollu_mu)
    async def hg(self, ctx, *args):
        await ctx.send(padisah_fermani)

    @command()
    @check(izinli_rollu_mu)
    async def onay(self, ctx):
        if len(ctx.message.mentions) > 0:
            try:
                uye: discord.member.Member = ctx.message.mentions[0]
                
                tp_uyesi_rolu = discord.utils.get(uye.guild.roles, id=900647464342790204)
                await uye.add_roles(tp_uyesi_rolu)
            
                await thumbs_up(ctx)
            except:
                await thumbs_down(ctx)
        else:
            await thumbs_down(ctx)
        await ctx.message.delete(delay=8)

Onayci("TPBOT_TOKEN_NAZGUL_1", Onayci.__name__)