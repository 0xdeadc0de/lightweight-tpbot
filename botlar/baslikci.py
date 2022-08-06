from discord import Message
from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class Baslikci(Cogcu):
    @Cog.listener("on_message")
    async def yarat(self, ctx: Message):
        if 120 != ctx.channel.slowmode_delay:
            return
        await ctx.create_thread(name="Yorumlar 👉")

def main():
    Baslikci("TPBOT_TOKEN_NAZGUL_1", Baslikci.__name__.lower())
if __name__ == "__main__":
    main()