from alayina_gider import Arayuzcu, Kanal
from discord.ext.commands import *
import discord
from baslayacagim import Baslayacagim

class ArayuzNazgul(Arayuzcu):
    
    baslik = ""
    kanal_id = Kanal.BotKomutlar.id
    def embedler(self):
        embed=discord.Embed(
            description=
f"""_Yol üzerinde yürürken birden etrafını karanlıklar sardı ve yolunu süliyeti belirsiz bir atlı sürücü kesiverdi.
Simsiyah pelerin ve çarşafa bürünmüş bu varlık yavaşçana suratını sana doğru çevirdi ve gülümsedi_
`{self.bot.user.display_name}:`
"""
        )
        #embed.add_field(name=f"`{self.bot.user.display_name}:`", value=f"```Nasıl yardımcı olabilirim?```")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar.url)
        embed.set_image(url="https://media2.giphy.com/media/W62wk6w0VI55Ijcnva/giphy.gif?cid=790b7611bff8340e5b25e79b3d4bb4cf177efb5725b6ba9d&rid=giphy.gif&ct=g")
        return [embed]

    class Arayuz(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            self.bot = bot
            super().__init__(*items, timeout=timeout)

        @discord.ui.button(label="Programlamaya nasıl başlarım yardımcı olabilir misin?", style=discord.ButtonStyle.secondary)
        async def bc1(self, button, interaction: discord.Interaction):
            await Baslayacagim.baslayacagim(self, interaction)

def main():
    ArayuzNazgul("TPBOT_TOKEN_NAZGUL_1", ArayuzNazgul.__name__.lower())
if __name__ == "__main__":
    main()