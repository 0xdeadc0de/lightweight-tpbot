import discord
from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class Kodcu(Cogcu):
    @Cog.listener()
    async def on_presence_update(self, before, after):

        icrawl = 383226320970055681
        add = any(hasattr(x, "application_id") and x.application_id == icrawl for x in after.activities)
        uye = discord.utils.get(after.guild.members, id=after.id)
        kodluyor = discord.utils.get(after.guild.roles, id=859338500494327810)
        if add:
            await uye.add_roles(kodluyor)
        else:
            await uye.remove_roles(kodluyor)


def main():
    Kodcu("TPBOT_TOKEN_NAZGUL_1", Kodcu.__name__.lower())
if __name__ == "__main__":
    main()
