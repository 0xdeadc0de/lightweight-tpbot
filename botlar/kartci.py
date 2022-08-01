from kartci_yazi import kartlar
from kartci_nitelik import CardPlayKind, CardRarity, CardTitle
import discord
from alayina_gider import Cogcu, idler
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

class Kartci(Cogcu):
    @slash_command(guild_ids=[idler.sunucu], description="TP destesinden bir kart oynar.")
    @cooldown(1, 60, BucketType.user)
    @option("kart no", description="hangi kart oynancak?")
    async def kart(self, ctx: discord.ApplicationContext, no: int):
        if no <= 0 or no > len(kartlar):
            await ctx.respond("Geçersiz kart no", ephemeral=True)
        else:
            await ctx.respond("`"+ctx.author.display_name + " bir kart oynadı.`", embeds=[cardGosterEmbed(no)],ephemeral=False)
    
    @slash_command(guild_ids=[idler.sunucu], description="TP destesine gözat.")
    async def deste(self, ctx):
        await ctx.respond("```css\n"+"\n".join([str(k+1)+". "+v.baslik for k, v in enumerate(kartlar)])+"```", ephemeral=True)
    

    @Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            await ctx.respond(error, ephemeral=True)
        else:
            raise error

Kartci("TPBOT_TOKEN_NAZGUL_1", Kartci.__name__.lower())