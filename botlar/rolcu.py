from pydoc import describe
from discord import Interaction, SlashCommandGroup
import discord
from alayina_gider import Cogcu, idler, interaction_member
from discord.ext.commands import *

def secim(select):
    secim = None
    for k, v in enumerate(select.options):
        if v.value == select.values[0]:
            secim = k
            break
    if secim is None:
        bot.gunluk("sacma sapan seyler oluyor bir bakarsin")
        raise
    return secim
class Rolcu(Cogcu):

    rol = SlashCommandGroup(name="rol", description="roller kanalı dışında alınabilecek diğer tüm roller", guild_ids=[idler.sunucu])
    class Egitim(discord.ui.View):
        @discord.ui.select(min_values = 1, max_values = 1,
            placeholder = "Okuduğunuz veya mezun olduğunuz eğitim seviyesini seçiniz.",
            options = [
                discord.SelectOption(label="Lise"),
                discord.SelectOption(label="Üniversite"),
                discord.SelectOption(label="Yüksek Lisans"),
                discord.SelectOption(label="Doktora"),
                discord.SelectOption(label="--Rolü temizle--"),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction):
            roller = [
                "1003759942878101564",
                "1003760022087540867",
                "1003760025673662655",
                "1003761421886165112",
            ]
            uye = interaction_member(interaction)
            if uye is None:
                return

            roller = list(filter(lambda m: str(m.id) in roller, uye.guild.roles))
            await uye.remove_roles(*roller)
            secildi = secim(select)
            if secildi!=4:
                await uye.add_roles(roller[secildi])
            await interaction.response.edit_message(content=f"Seçtiğiniz işlem gerçekleştirildi.")

    @rol.command(description="Okuduğunuz veya mezun olduğunuz eğitim seviyesini seçiniz.")
    async def egitim(self, ctx):
        await ctx.respond(ephemeral=True, view=__class__.Egitim())

    
    class Durum(discord.ui.View):
        @discord.ui.select(min_values = 1, max_values = 1,
            placeholder = "Okuduğunuz veya mezun olduğunuzu belirtin.",
            options = [
                discord.SelectOption(label="Okuyorum"),
                discord.SelectOption(label="Mezunum"),
                discord.SelectOption(label="--Rolü temizle--"),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction):
            roller = [
                "1003760028693569616",
                "1003759998297456720",
            ]
            uye = interaction_member(interaction)
            if uye is None:
                return

            roller = list(filter(lambda m: str(m.id) in roller, uye.guild.roles))
            await uye.remove_roles(*roller)
            secildi = secim(select)
            if secildi!=2:
                await uye.add_roles(roller[secildi])
            await interaction.response.edit_message(content=f"Seçtiğiniz işlem gerçekleştirildi.")

    @rol.command(description="Okuduğunuz veya mezun olduğunuzu belirtin.")
    async def durum(self, ctx):
        await ctx.respond(ephemeral=True, view=__class__.Durum())

    @Cog.listener("on_raw_reaction_add")
    @Cog.listener("on_raw_reaction_remove")
    async def ne(self, payload: discord.RawReactionActionEvent):
        # https://github.com/turkprogramcilar/tpbot/blob/master/greenfield/v2/modules/freestyle/legacy/discordbot/modules/bilenrol.ts
        # dosyasindan cevrilmistir

        if payload.channel_id != 868227685636263956 or payload.emoji.name is None:
            return

        class role_type:
            language = 0
            fan_club = 1
        
        language_roles = [
            "xml", "angular", "aspnet", "bootstrap", "css", 
            "clang", "cplusplus", "csharp", "django", "ecmascript", 
            "flutter", "fsharp", "go", "godot", "haskell",
            "html", "java", "javascript", "kotlin", "laravel", 
            "lua", "mongodb", "mssql", "mysql", "nodejs", 
            "perl", "php", "python", "react", "ruby",
            "rust", "sql", "typescript", "unity", "unrealengine", 
            "visualbasic"
        ]
        fan_club_roles = ["ricardo", "risitas", "ibo"]
        language_roles_custom = {
            "microsoft": "mssql",
            "👢": "bootstrap",
            "🎯": "dart",
            "logo_django2": "django",
        }
        #// test to see if these are allowed roles
        type = None
        role = payload.emoji.name.lower()
        if role in language_roles_custom.keys():
            role = language_roles_custom[role]
            type = role_type.language
        
        elif role in language_roles:
            type = role_type.language
        
        elif role in fan_club_roles:
            type = role_type.fan_club
        
        else:
            self.gunluk("not allowed role: "+role)
            return
        
        role = role.capitalize()

        role_postfix = {
            role_type.fan_club: " Fan",
            role_type.language: "",
        }

        role_name = f"{role}{role_postfix[type]}"

        uye = payload.member
        if uye is None:
            guild = await self.bot.fetch_guild(payload.guild_id)
            uye = await guild.fetch_member(payload.user_id)
                
        tp_uyesi_rolu = discord.utils.get(uye.guild.roles, name=role_name)
        if tp_uyesi_rolu is None:
            self.bot.gunluk("yeni rol olusturulmadi =>", tp_uyesi_rolu)
            return
        
        if payload.event_type == "REACTION_ADD":
            await uye.add_roles(tp_uyesi_rolu)
        else:
            await uye.remove_roles(tp_uyesi_rolu)

def main():
    Rolcu("TPBOT_TOKEN_NAZGUL_1", Rolcu.__name__.lower())
if __name__ == "__main__":
    main()