from alayina_gider import Arayuzcu, Kanal, embed_sohbet
from discord.ext.commands import *
import discord
from baslayacagim import Baslayacagim
from kartci import Kartci

class ArayuzNazgul(Arayuzcu):
    
    baslik = ""
    kanal_id = Kanal.NazgulRicardo.id
    def embedler(self):
        return([embed_sohbet(self.bot.user, 
            dis_ses=f"""_Yol üzerinde yürürken birden etrafını karanlıklar sardı ve yolunu süliyeti belirsiz bir atlı sürücü kesiverdi.
Simsiyah pelerin ve çarşafa bürünmüş bu varlık yavaşçana suratını sana doğru çevirdi ve gülümsedi_""", )])

    class Arayuz(discord.ui.View):
        def __init__(self, *items, timeout = None, bot = None):
            self.bot = bot
            super().__init__(*items, timeout=timeout)

        @discord.ui.button(label="Programlamaya nasıl başlarım yardımcı olabilir misin?", style=discord.ButtonStyle.secondary, row=1)
        async def _1(self, button, interaction: discord.Interaction):
            await Baslayacagim.baslayacagim(self, interaction)

        @discord.ui.button(label="Sihirli bir kartı nasıl oynayabilirim?", style=discord.ButtonStyle.blurple, row=0)
        async def _2(self, button, interaction: discord.Interaction):
            class Devam(discord.ui.View):
                def __init__(self, *items, timeout = None, bot = None):
                    self.bot = bot
                    super().__init__(*items, timeout=timeout)
                @discord.ui.button(label="Bahsettiğin güç hakkında bilgi verebilir misin?", style=discord.ButtonStyle.secondary, row=0)
                async def _1(self, button, interaction: discord.Interaction):
                    await interaction.response.send_message(
                        ephemeral=True,
                        embed=embed_sohbet(self.bot.user, konusma=
f"""Bu güç Türk Programcılar diyarındaki diğer kıymet teşkil eden madenlere benzemez, senin içine nüfus eder ve \
hiçkimse senden bu gücü alamaz veya gasp edemez. `Karanlık Güç Token (KGT)`'ına sahip kişiler ancak bu güce erişebilirler ve
bu güç onları daha da saldırgan hale getirir.

Gün aşırı <#{Kanal.BugunNeYaptim.id}> diyarındaki gönderisi üzerine açılan başlığa ` !kgt ` komutunu \
çalıştırdığı zaman 23 saat içerisinde bir Nazgul'ün karanlık gölgesi tarafından sarmalanır ve \
bu token ona nüfus eder."""))

            await interaction.response.send_message(
                view=Devam(bot=self.bot),
                ephemeral=True,
                embed=embed_sohbet(self.bot.user, konusma=
"""Öncelikle bazı kartlar için yeterli gücün olduğuna emin olmalısın. Çoğu barışçıl kart için buna ihtiyacın olmayacak.

Daha sonra kart numaranı belirledikten sonra ` /kart ` yazıp oynamak istediğin kart numarasını yazmalısın. \
Kartı oynamadan önce göz atmak için ` /gozat ` komutunu kullanabilirsin. Böylece doğru kartı oynadığından emin olabilirsin.

Kart numaraları hakkında bilgi almak için ` /deste ` komutunu kullanabilirsin veya istediğin zaman bana sorabilirsin."""))

        @discord.ui.button(label="Sihirli kart numaraları hakkında bilgin var mı?", style=discord.ButtonStyle.secondary, row=0)
        async def _3(self, button, interaction: discord.Interaction):
            await Kartci.deste(self, interaction)

def main():
    ArayuzNazgul("TPBOT_TOKEN_NAZGUL_2", ArayuzNazgul.__name__.lower())
if __name__ == "__main__":
    main()