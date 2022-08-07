from kartci_yazi import kartlar
from kartci_nitelik import CardPlayKind, CardRarity, CardTitle
import discord
from alayina_gider import Cogcu, idler, cevap, Rol
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
    @slash_command(guild_ids=[idler.sunucu], description="TP destesinden bir kart gösterir.")
    @cooldown(1, 15, BucketType.user)
    @option("kart no", description="hangi kart gösterilecek?")
    async def kart(self, ctx: discord.ApplicationContext, no: int):
        if no <= 0 or no > len(kartlar):
            await ctx.respond("Geçersiz kart no", ephemeral=True)
        else:
            if ctx.channel.permissions_for(ctx.author).view_channel and ctx.channel.permissions_for(ctx.author).send_messages:
                await ctx.respond("`"+ctx.author.display_name + " bir kart gösterdi.`", embeds=[cardGosterGifli(no)],ephemeral=False)
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
    
    @slash_command(guild_ids=[idler.sunucu], description="TP destesine gözat.")
    async def deste(self, ctx):
        await cevap(ctx)("```css\n"+"\n".join([str(k+1)+". "+v.baslik for k, v in enumerate(kartlar)])+"```", ephemeral=True)

def main():
    Kartci("TPBOT_TOKEN_NAZGUL_2", Kartci.__name__.lower())
if __name__ == "__main__":
    main()