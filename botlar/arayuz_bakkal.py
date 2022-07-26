from dis import dis
from alayina_gider import Arayuzcu, Kanal, embed_sohbet
from discord.ext.commands import *
import discord
from baslayacagim import Baslayacagim
from kartci import Kartci
from bakkal import Bakkal
from ekonomici import Ekonomici

class ArayuzBakkal(Arayuzcu):
    
    baslik = ""
    kanal_id = Kanal.BakkalRisitas.id
    def embedler(self):
        return([embed_sohbet(self.bot.user, 
            dis_ses=f"""_Türk Programcılar diyarında dolaşırken dar sokaklar arasından bir küçük dükkanda kendi halinde köşesine \
çekilmiş tıfıl bir adam ile karşılaştın. 

Elindeki bir keseden hışırtılı bir şekilde teker teker çıkarttığı madeni paraları sayarken birden göz göze geliverdin_""",balon=
"""Zamanımı harcama. Vakit nakittir. Ne istiyorsun söyle."""
        )])

    class Arayuz(discord.ui.View):
        def __init__(self, *items, timeout = None, bot = None):
            self.bot = bot
            super().__init__(*items, timeout=timeout)

        @discord.ui.button(label="Bu madeni paralar hakkında bilgi verebilir misin?", style=discord.ButtonStyle.secondary, row=0)
        async def _1(self, button, interaction: discord.Interaction):
            embed=embed_sohbet(self.bot.user, konusma=
f"""Türk Programcılar diyarında üç çeşit madeni para vardır. 

Birincisi `Risitas Coin (RSC)`.
İkincisi ise `Ricardo Coin (RCC)`. 
Üçüncüsü ise `İbo Coin (İBO)`dir.

Bu topraklarda belirli aktiviteler sonucu bu madeni paralardan kazanma şansın vardır.""")
            class Devam(discord.ui.View):
                def __init__(self, *items, timeout = None, bot = None):
                    self.bot = bot
                    super().__init__(*items, timeout=timeout)
                @discord.ui.button(label="Ricardo Coin (RCC) hakkında bilgi verebilir misin?", style=discord.ButtonStyle.secondary, row=0)
                async def _1(self, button, interaction: discord.Interaction):
                    embed=embed_sohbet(self.bot.user, konusma=
f"""Sunucu içerisindeki her bir üye yeteri kadar uzun mesaj gönderdiğinde `1 RCC dinarı` kazanırlar.

Ayrıca başlık içerisinde gönderdikleri mesaj spam olmadığı sürece belirli bir şans ile ekstra `1 RCC dinarı` daha kazanırlar. \
Dolayısı ile her bir başlık mesajı `2 RCC dinarı` kazanma şansı vardır.""")
                    await interaction.response.send_message(ephemeral=True, embed=embed)

                @discord.ui.button(label="Risitas Coin (RSC) hakkında bilgi verebilir misin?", style=discord.ButtonStyle.secondary, row=1)
                async def _2(self, button, interaction: discord.Interaction):
                    embed=embed_sohbet(self.bot.user, konusma=
f"""<#{Kanal.Bumperado.id}> diyarında bump yapılanlar Ekselans Risitas tarafından `100 RSC` ile şereflendirilirler. \
Unutma her iki saatte bir sadece bir kişi bu ödüle ulaşabilir. \
O yüzden bu ödülü kazanbilmek için sunucuyu çok iyi takip etmen gerekir.

Paylaşım kategorisinde paylaşımda bulunan üyeler `1 Risitas Coin` kazanırlar.

<#{Kanal.BugunNeYaptim.id}> gününü değerlendiren ve kanal formatına uyan üyeler tamı tamına `500 Risitas Coin` kazanırlar. \
Bu kazanabileceğin en yüksek miktardaki ödüldür. O yüzden her günün sonunda <#{Kanal.BugunNeYaptim.id}> diyarını ziyaret \
etmeyi kesinlikle unutma.

Şimdilik sana öğreteceklerim bu kadar. Ha birde unutmadan... Moderatör gözlerin belirli durumlarda Risitas Coin ödülü verme hakları vardır. \
Bunlardan ilk ve en önemlisi <#{Kanal.GununSorusu.id}> diyarında günlük leetcode sorularıyla savaşmak. İkincisi ise \
sunucu içerisinde örnek bir üye olmaktır.""")
                    await interaction.response.send_message(ephemeral=True, embed=embed)

                @discord.ui.button(label="İbo Coin (İBO) hakkında bilgi verebilir misin?", style=discord.ButtonStyle.secondary, row=2)
                async def _3(self, button, interaction: discord.Interaction):
                    embed=embed_sohbet(self.bot.user, konusma=
f"""Türk Programcılar krallığında bu diyara özel tanımlanmış sunucu emojilerinin kullanımı yaygındır.

<#{Kanal.EmojiKatalogu.id}> sokağına gidersen burada tanımlanan özel sunucu emojilerini bulabilirsin. \
Bu kategoride bulunan İbo emojilerinin kullanımı belirli bir şans ile `1 İbo Coin` kazandırır. \
Arkadaşlarınla sohbet ederken kendini ifade etmek için standart emojiler yerine buradaki emojileri kullanmalısın \
ki bu madeni sık sık kazanasın.

Ayrıca... Bir söylentiye göre de bu diyarda Efsanevi İbo adında esrarengiz bir varlık gördüğü kişilere çok yüklü miktarda \
İbo Coin armağan edermiş. Şu güne kadar buna tanıklık ettiğini söyleyen bir kaç kişi dükkanımı ziyaret etti fakat şahsen ben \
anlatılan hikayelerin masal olduğuna inanıyorum. Kim bilir belki bir gün sen karşılaşırsın ve bana bu karakter hakkında daha fazla \
bilgi verirsin!""")
                    await interaction.response.send_message(ephemeral=True, embed=embed)
            # devam sonu

            await interaction.response.send_message(ephemeral=True, embed=embed, view=Devam(bot=self.bot))

        @discord.ui.button(label="Senin saydıklarına benzer bir kaç madeni param var.", style=discord.ButtonStyle.secondary, row=0)
        async def _2(self, button, interaction: discord.Interaction):
            await interaction.response.send_message(
                ephemeral=True,
                embed=embed_sohbet(self.bot.user, resim="https://media3.giphy.com/media/KDhwDeTh245v0KnLeO/giphy.gif?cid=790b76112668610765b6d60a5705d3bb0444059d47b21582&rid=giphy.gif&ct=g",
                 dis_ses=f"""`{self.bot.user.display_name}:`
Hmm. Gözlerim beni yanıltmıyorsa bunlar El Risitas krallığına ait dinarlar olsa gerek. 

Şu tarafta toparlanmış olanlar da Nazgul Ricardo'ya ait para birimi.

Elinde ne kadar dinar olduğunu saymak istiyorsan <#{Kanal.BotKomutlar.id}> diyarına gidip ` !{Ekonomici.bakiye.name} ` komutunu çalıştırman gerek.

Unutma, öncelikle kazandığın dinarların aktarımını ` !{Ekonomici.paraciklar.name} ` komutuyla yapmalısın aksi taktirde eksik sayım çıkacaktır.
"""))
    
        @discord.ui.button(label="Dükkana göz at", style=discord.ButtonStyle.blurple, row=1)
        async def _3(self, button, interaction: discord.Interaction):
            await Bakkal.bakkal(self, interaction)

def main():
    ArayuzBakkal("TPBOT_TOKEN_BAKKAL", ArayuzBakkal.__name__.lower())
if __name__ == "__main__":
    main()