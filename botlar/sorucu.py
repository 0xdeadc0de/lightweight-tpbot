import io
import discord
from alayina_gider import Cogcu, Kanal, idler, Rol
from discord.commands import *
from discord.ext.commands import *

padisah_fermani = """Bu başlık altından sorunuzu sorunuz.
Lütfen aşağıdaki maddeleri gözden geçirerek sorunuzun uygunluğundan emin olun. Bu yayınlanma sürecini hızlandıracaktır.

1-> <#827892178561925160> uygun soru sordugunuzdan emin olun

2-> <#856106750573936660> ya uygun olmali

Sorunuzu bu başlık altında düzenlemeye devam edebilirsiniz. 
İncelendikten sonra bir eksik yok ise sorunuz en kısa sürede onaylanacaktır. Bir eksik çıktığı taktirde sizinle bu sayfa üzerinden iletişime geçilecek ve eksiklerinizi düzeltmeniz istenecektir. İyi kodlar dileriz. 
-TP Yönetim <@&826741535839748096> <@&830478022183616564>
"""
class Sorucu(Cogcu):
    @Cog.listener()
    async def on_message(self, ctx):
        if ctx.channel.id != Kanal.SoruSor.id:
            return

        baslik = await ctx.create_thread(name="Sorma süreci 👉")
        if baslik is None:
            return

        await baslik.send(padisah_fermani)
        await ctx.delete()

    @message_command(guild_ids=[idler.sunucu], name="soru kopyala")
    @Rol.AsistanEditorKurucuMu()
    async def caliskanim(self, ctx: discord.ApplicationContext, message):
        yazi=message.content
        baytlarlaylay = yazi.encode(encoding="utf8")
        fp=io.BytesIO(baytlarlaylay)
        await ctx.respond(file=discord.File(fp, "mesaj.txt"), ephemeral=True)

Sorucu("TPBOT_TOKEN_NAZGUL_1", Sorucu.__name__.lower())