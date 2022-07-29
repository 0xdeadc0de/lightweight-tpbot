from discord import Message
from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class baslikci(Cogcu):
    @Cog.listener("on_message")
    async def yarat(self, ctx: Message):
        if 120 != ctx.channel.slowmode_delay:
            return
        await ctx.create_thread(name="Yorumlar 👉")

baslikci("TPBOT_TOKEN_NAZGUL_1", baslikci.__name__)