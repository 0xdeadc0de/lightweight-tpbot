from alayina_gider import Arayuzcu, Kanal
from discord.ext.commands import *
import discord

class TestciArayuz(Arayuzcu):
    
    baslik = ""
    kanal_id = Kanal.BotKomutlar.id
    def embedler(self):
        embed=discord.Embed(
            description="```Size nasıl yardımcı olabilirim?```",
        )
        embed.add_field(name="`Risitas Coin (RSC)`", value=f"```22```")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_author(name=self.bot.user.display_name, icon_url=self.bot.user.display_avatar.url)
        return [embed]
    class Arayuz(discord.ui.View):
        @discord.ui.button(label="Cüzdanına göz at", style=discord.ButtonStyle.secondary, emoji="💵")
        async def bc1(self, button, interaction):
            await interaction.response.send_message("Az bekle!", ephemeral=True)

        @discord.ui.button(label="Coin topla", style=discord.ButtonStyle.secondary, emoji="🪙")
        async def bc2(self, button, interaction):
            await interaction.response.send_message("Bekleyen coin'iniz bulunmamaktadır!", ephemeral=True)

def main():
    TestciArayuz("TPBOT_TOKEN_TEST", TestciArayuz.__name__.lower())
if __name__ == "__main__":
    main()
