from kartci_yazi import kartlar
from kartci_nitelik import CardPlayKind, CardRarity, CardTitle
import discord
import math
from mangocu import Mangocu
from alayina_gider import Cogcu, idler, cevap, Rol, embed_sohbet
from discord.commands import *
from discord.ext.commands import *

def kodBlogu(format, yazi):
    return f"```{format}\n{yazi}```"


renkler = {
    CardRarity.Yaygın: [88,  110, 117],
    CardRarity.Esrarengiz: [131, 148, 150],
    CardRarity.Güzide: [42,  161, 152],
    CardRarity.İhtişamlı: [181, 137, 0],
    CardRarity.Destansı: [203, 75,  22]
}
def rgb(renk):
    return (renk[0] << 16) + (renk[1] << 8) + renk[2]
formatlar = {
    CardRarity.Yaygın: "brainfuck",
    CardRarity.Esrarengiz: "",
    CardRarity.Güzide: "yaml",
    CardRarity.İhtişamlı: "fix",
    CardRarity.Destansı: "css"
}

def cardGosterEmbed(no):
    kart = kartlar[no-1]
    embed = discord.Embed(
        title=f"`{kart.baslik}`",
        description=kodBlogu(formatlar[kart.cins], f"[{kart.aciklama}]"),
        fields=[
            discord.EmbedField(name=f"`Kart cinsi: {kart.cins}`", value =f"No: {no}\n\n\n")
        ],
        color=discord.Color(rgb(renkler[kart.cins]))
    )
    embed.set_thumbnail(url=kart.link)
    return embed

def cardGosterGifli(no):
    embed=cardGosterEmbed(no)
    embed.set_image(url=embed.thumbnail.url)
    embed.remove_thumbnail()
    return embed

class Kartci(Cogcu):
    @slash_command(guild_ids=[idler.sunucu], description="Koleksiyonundan bir kart gösterir.")
    @cooldown(1, 15, BucketType.user)
    @option("kart no", description="hangi kart gösterilecek?")
    async def kart(self, ctx: discord.ApplicationContext, no: int):
        if no <= 0 or no > len(kartlar):
            await ctx.respond("Geçersiz kart no", ephemeral=True)
        else:
            if ctx.channel.permissions_for(ctx.author).view_channel and ctx.channel.permissions_for(ctx.author).send_messages:
                if Mangocu.sikleton().uye(ctx.author.id).varmi(f"kart_{no}"):
                    await ctx.respond("`"+ctx.author.display_name + " bir kart gösterdi.`", embeds=[cardGosterGifli(no)],ephemeral=False)
                else:
                    await ctx.respond("Destenizde belirtilen numaradaki karttan yok", ephemeral=True)
            else:
                await ctx.respond("Bu kanala kart gönderemezsiniz", ephemeral=True)

    @slash_command(guild_ids=[idler.sunucu], description="TP destesinden bir karta göz at.")
    @cooldown(1, 15, BucketType.user)
    @option("kart no", description="hangi kart gösterilecek?")
    async def gozat(self, ctx: discord.ApplicationContext, no: int):
        if no <= 0 or no > len(kartlar):
            await ctx.respond("Geçersiz kart no", ephemeral=True)
        else:
            await ctx.respond(embeds=[cardGosterEmbed(no)],ephemeral=True)
    
    en_uzun = None
    @slash_command(guild_ids=[idler.sunucu], description="Kart koleksiyonuna göz at.")
    @cooldown(1, 15, BucketType.user)
    async def koleksiyon(self, ctx: discord.ApplicationContext):
        uye=Mangocu.sikleton().uye(ctx.author.id).bul()
        if uye is None:
            await ctx.respond("Koleksiyonunuz boş", ephemeral=True)
            return

        if Kartci.en_uzun is None:
            Kartci.en_uzun = len(max(kartlar, key=lambda x: len(x.baslik)).baslik)
        koleksiyon=[
            (kartlar[no-1].baslik.ljust(Kartci.en_uzun)+f"({no}): ".rjust(3+4) + str(uye.get(f"kart_{no}") or '-').ljust(3))
            for no in range(1, 1+len(kartlar))
        ]
        if len(koleksiyon)==0:
            await ctx.respond("Koleksiyonunuz boş", ephemeral=True)
            return
        ayir = 2
        alan = math.ceil(len(koleksiyon)/ayir)
        ayrik = [koleksiyon[x*alan:(x+1)*alan] for x in range(ayir)]
        birlesik = [" | ".join(ayri) for ayri in zip(*ayrik)]

        alan /= ayir #yetecektir discord 1024 limiti icin...
        alan = int(alan)
        butun = ["```"+("\n".join(birlesik[x*alan:(x+1)*alan]))+"```" for x in range(ayir)]

        for x in butun:
            await ctx.respond(ephemeral=True, content=x)
    

    @slash_command(guild_ids=[idler.sunucu], description="TP destesine gözat.")
    async def deste(self, ctx):
        await cevap(ctx)("```css\n"+"\n".join([str(k+1)+". "+v.baslik for k, v in enumerate(kartlar)])+"```", ephemeral=True)

def main():
    Kartci("TPBOT_TOKEN_NAZGUL_2", Kartci.__name__.lower())
if __name__ == "__main__":
    main()