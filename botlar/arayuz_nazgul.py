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
Simsiyah pelerin ve çarşafa bürünmüş bu varlık yavaşçana suratını sana doğru çevirdi ve gülümsedi_
`{self.bot.user.display_name}: ?`""", )])

    class Arayuz(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            self.bot = bot
            super().__init__(*items, timeout=timeout)

        @discord.ui.button(label="Programlamaya nasıl başlarım yardımcı olabilir misin?", style=discord.ButtonStyle.secondary, row=0)
        async def _1(self, button, interaction: discord.Interaction):
            await Baslayacagim.baslayacagim(self, interaction)

        @discord.ui.button(label="Sihirli bir kartı nasıl oynayabilirim?", style=discord.ButtonStyle.secondary, row=1)
        async def _2(self, button, interaction: discord.Interaction):
            await interaction.response.send_message(
                ephemeral=True,
                embed=embed_sohbet(self.bot.user, konusma=
"""Öncelikle sihirli bir kart oynamak için yeterli gücün olduğuna emin olmalısın.

Daha sonra kart numaranı belirledikten sonra /kart yazıp oynamak istediğin kart numarasını yazmalısın.

Kart numaraları hakkında bilgi almak için /deste komutunu kullanabilirsin veya istediğin zaman bana sorabilirsin."""))

        @discord.ui.button(label="Sihirli kart numaraları hakkında bilgin var mı?", style=discord.ButtonStyle.secondary, row=1)
        async def _3(self, button, interaction: discord.Interaction):
            await Kartci.deste(self, interaction)

def main():
    ArayuzNazgul("TPBOT_TOKEN_NAZGUL_1", ArayuzNazgul.__name__.lower())
if __name__ == "__main__":
    main()