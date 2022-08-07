import discord
from mangocu import Mangocu
from kartci_yazi import kartlar, CardText
from alayina_gider import Cogcu, yonetici_mi, Yonetici, Kanal, DEBUG
from discord.ext.commands import *

class Kartoyna(Cogcu):
    @Cog.listener()
    async def on_ready(self):
        self.mango = Mangocu.sikleton()

    async def gunce(self, ctx: discord.ApplicationContext, hedef: discord.User, kart: CardText, mesaj):
        
        kanal: discord.TextChannel = discord.utils.get(ctx.guild.channels, id=Kanal.TpbotTest1.id if DEBUG() else Kanal.Gunce.id)
        if kanal is None: return
        dis_ses = f"_...Destesinden **{kart.baslik}** adlı kartını aldı ve cebinden çıkarttığı \
            `Karanlık Güç Token`ına doğru yaklaştırdı. Güç elinde yoğunlaşırken kartın üzerindeki kelimeler sırayla ışıldamaya başladı. \
            Ardından yüzüne doğru yaklaştırdığı karta hedefinin ismini kısık bir sesle fısıldadı. `{hedef.display_name}!` Daha sonra kartı ileriye doğru bıraktı._"
                
        embed=discord.Embed(description=dis_ses)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        embed.set_thumbnail(url=hedef.display_avatar.url)
        embed.add_field(inline=False, name="`Kartın sonuçları`", value=mesaj)
        await kanal.send(embed=embed)

    
    @slash_command(description="koleksiyonunuzda bulunan kartlardan hedef seçimli oynar")
    @cooldown(1, 15, BucketType.user)
    async def oyna(self, ctx: discord.ApplicationContext, 
        uye: discord.Option(discord.Member, "kartın özelliğine göre hedefe zarar veya şifa verebilir"),
        no: discord.Option(int, "oynancak kart numarası")
    ):
        if no <= 0 or no > len(kartlar):
            await ctx.respond("Geçersiz kart no", ephemeral=True)
            return
        
        if self.mango.uye(ctx.author.id).deste().varsa_azalt(no):
            await ctx.respond("Kart oynandı", ephemeral=True)
            await self.gunce(ctx, uye, kartlar[no-1], "OK")
        else:
            await ctx.respond("Destenizde belirtilen numaradaki karttan yok", ephemeral=True)
        
def main():
    Kartoyna("TPBOT_TOKEN_NAZGUL_3", Kartoyna.__name__.lower())
if __name__ == "__main__":
    main()