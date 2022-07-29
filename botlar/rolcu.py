from discord import Interaction
import discord
from alayina_gider import Cogcu
from discord.ext.commands import *

class Rolcu(Cogcu):
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
        fan_club_roles = ["ricardo", "risitas"]
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
            role_type.fan_club: "Fan",
            role_type.language: "Bilen",
        }

        role_name = f"{role} {role_postfix[type]}"

        uye = payload.member
        if uye is None:
            guild = await self.bot.fetch_guild(payload.guild_id)
            uye = await guild.fetch_member(payload.user_id)
                
        tp_uyesi_rolu = discord.utils.get(uye.guild.roles, name=role_name)
        if tp_uyesi_rolu is None:
            self.gunluk("yeni rol olusturulmadi =>", tp_uyesi_rolu)
            return
        
        if payload.event_type == "REACTION_ADD":
            await uye.add_roles(tp_uyesi_rolu)
        else:
            await uye.remove_roles(tp_uyesi_rolu)

Rolcu("TPBOT_TOKEN_NAZGUL_1", Rolcu.__name__.capitalize())