import discord
from discord import Message
from alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class Baslikci(Cogcu):
    @Cog.listener("on_message")
    async def yarat(self, ctx: Message):
        if type(ctx.channel) is not discord.TextChannel:
            return
        if 120 != ctx.channel.slowmode_delay:
            return
        await ctx.create_thread(name="Yorumlar 👉", auto_archive_duration=60)

def main():
    Baslikci("TPBOT_TOKEN_NAZGUL_1", Baslikci.__name__.lower())
if __name__ == "__main__":
    main()