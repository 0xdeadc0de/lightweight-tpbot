izinli_roller = [
    801135743229624320, #KURUCU
    830478022183616564, #EDITOR
    826741535839748096, #ASISTAN
]
def izinli_rollu_mu(ctx):
    return any(rol.id in izinli_roller for rol in ctx.author.roles)

padisah_fermani = """Merhaba hoş geldiniz. Sizlere bir kaç sorumuz olacak. Lütfen sırayla cevaplayınız.

1) Sunucuyu nereden (kimden, nasıl, disboard vb..) buldunuz. DISBOARD ise DISBOARD yazın. İnternet'ten bulduysanız ve DISBOARD değilse bulduğunuz sitenin isminiz yazınız.

2) Gelme amacınız nedir?

3) Programlama ile ilgileniyor musunuz?

4) Neleri biliyorsunuz?

5) Son aldığınız eğitim lise, üniv v.b (opsiyonel olarak yaş ekleyebilirsiniz)?

6) <#1005537084267831407> kanalına gidip [Programlamaya nasıl başlarım yardımcı olabilir misin?] yazılı mavi tuşa basıp, adımları tamamladıktan sonra çıkan sonucu belirtin.

Cevaplarınızı verdikten sonra, cevaplarınızda bir eksik yok ise kaydınız en kısa sürede onaylanacaktır. Bir eksik çıktığı taktirde sizinle bu sayfa üzerinden iletişime geçilecek ve eksiklerinizi düzeltmeniz istenecektir. İyi kodlar dileriz. 
-TP Yönetim <@1001882496549527553>"""

import discord
from alayina_gider import Cogcu, Kanal, thumbs_down, thumbs_up, idler, Rol
from discord.ext.commands import *

class Onayci(Cogcu): 

    @Cog.listener()
    async def on_message(self, ctx):
        if ctx.channel.id != Kanal.MerhabaDunya.id:
            return

        baslik = await ctx.create_thread(name="Onay süreci 👉", auto_archive_duration=60)
        if baslik is None:
            return

        await baslik.send(f"<@{ctx.author.id}> "+padisah_fermani)
        await ctx.delete()

    async def onay_ver(self, uye: discord.member.Member):

        tp_uyesi_rolu = discord.utils.get(uye.guild.roles, id=900647464342790204)
        await uye.add_roles(tp_uyesi_rolu)

        
    @command()
    @check(izinli_rollu_mu)
    async def hg(self, ctx, *args):
        await ctx.send(padisah_fermani)

    @command()
    @check(izinli_rollu_mu)
    async def onay(self, ctx: Context):
        if len(ctx.message.mentions) > 0:
            try:
                
                uye: discord.member.Member = ctx.message.mentions[0]
                
                await self.onay_ver(uye)
            
                await thumbs_up(ctx)
            except:
                await thumbs_down(ctx)
        else:
            await thumbs_down(ctx)

        if ctx.channel.parent_id == Kanal.MerhabaDunya.id:
           await ctx.channel.archive(locked=True)

           
    @message_command(guild_ids=[idler.sunucu], name="onay ver")
    @Rol.AsistanEditorKurucuMu()
    async def caliskanim(self, ctx: discord.ApplicationContext, message: discord.message.Message):
        
        await ctx.send(f"Onay veriliyor... <@{message.author.id}>")
        msg=message.author.display_name
        try:
            await self.onay_ver(message.author)
            msg +=" onay verildi"
            await ctx.respond(msg, ephemeral=True)
            if ctx.channel.parent_id == Kanal.MerhabaDunya.id:
                await ctx.channel.archive(locked=True)
        except:
            msg +=" onay verilemedi "
            await ctx.respond(msg, ephemeral=True)

def main():
    Onayci("TPBOT_TOKEN_NAZGUL_1", Onayci.__name__.lower())
if __name__ == "__main__":
    main()
