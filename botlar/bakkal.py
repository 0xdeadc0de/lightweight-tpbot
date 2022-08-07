from collections import defaultdict
import discord
import random
import pymongo
from alayina_gider import Cogcu, TurkProgramcilar, Kanal, Rol, sunucu_uyesi, idler, cevap, embed_sohbet
from kartci_yazi import kartlar, CardText
from discord.ext.commands import *
from discord.ext.tasks import *
from mangocu import Mangocu

first=True
class Bakkal(Cogcu):
    @Cog.listener()
    async def on_ready(self):
        global first
        if not first: return; first = False
        self.mango = Mangocu.sikleton()

    @slash_command()
    async def bakkal(self, ctx):
        
        class Arayuz(discord.ui.View):
            def __init__(self, *items, timeout = None, bot = None):
                self.bot = bot
                super().__init__(*items, timeout=timeout)


            async def kart_al(self, interaction: discord.Interaction, carpan=1):

                uye=Mangocu.sikleton().uye(interaction.user.id)

                if not uye.hepsi_varsa_azalt({
                    #"ricardo_coin": 10*carpan,
                    "risitas_coin": 100*carpan,
                    #"ibo_coin": 10*carpan,
                }):
                    await interaction.response.send_message(ephemeral=True, embed=embed_sohbet(self.bot.user, 
                        konusma=f"Bakiyen yetersiz. Paran yoksa seninle vakit kaybedemem."))
                else:
                    paket=defaultdict(int)
                    for x in range(10*carpan):
                        paket[random.randint(1, len(kartlar))]+=1

                    uye.hepsini_ver({f"kart_{no}": adet for no, adet in paket.items()})
                    
                    await interaction.response.send_message(ephemeral=True, embed=embed_sohbet(self.bot.user, 
                        dis_ses=f"{10*carpan} kartlı paketi satin aldin. Paket içerisinden çıkanlar:", 
                        ozellikler={kartlar[no-1].baslik: adet for no, adet in paket.items()}))
                    

            @discord.ui.button(label="10'lu kart satın al", style=discord.ButtonStyle.gray, row=0)
            async def _1(self, button, interaction: discord.Interaction):

                await self.kart_al(interaction, carpan=1)


            @discord.ui.button(label="30'lu kart satın al", style=discord.ButtonStyle.gray, row=0)
            async def _2(self, button, interaction: discord.Interaction):
                
                await self.kart_al(interaction, carpan=3)


            @discord.ui.button(label="50'li kart satın al", style=discord.ButtonStyle.gray, row=0)
            async def _3(self, button, interaction: discord.Interaction):

                await self.kart_al(interaction, carpan=5)


        await cevap(ctx)(ephemeral=True, view=Arayuz(bot=self.bot), embed=embed_sohbet(self.bot.user, konusma=f"""Bu dükkanda ne arıyorsan bulabilirsin. Türk Programcılar diyarındaki en kaliteli ve ucuz mallar her zaman bendedir."""))

def main():
    Bakkal("TPBOT_TOKEN_BAKKAL", Bakkal.__name__.lower())
if __name__ == "__main__":
    main()