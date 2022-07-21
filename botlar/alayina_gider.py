yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
import time

import discord
import os
class Ebeveyn(discord.Client):
    def __init__(self, token_ismi) -> None:
        self.token_ismi = token_ismi
        self.gunluk("merhaba dünya! dosyamin ismi: ", __file__)
        super().__init__(intents=discord.Intents.all())
        token = os.environ.get(token_ismi)
        if token is None:
            self.gunluk(f"{token_ismi} degeri tanimli degil")
            exit(-1)
        self.run(token)

    def gunluk(self, *mesajlar):
        print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{self.token_ismi}]:", *mesajlar)

    async def on_ready(self):
        self.gunluk("atis serbest", self.user)

    async def on_message(self, message):
        
        if message.author == self.user or\
           message.author.id not in yoneticiler:
            return

        if message.content == '!ping':
            await message.channel.send(f'pong [{self.token_ismi}]')
            return

        if message.content.startswith("!kapan "):
            hedef = message.content[7:]

            if hedef == self.token_ismi:
                exit(1)
            return