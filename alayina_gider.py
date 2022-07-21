yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
import time
def gunluk(*mesajlar):
    print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{token_ismi}]:", *mesajlar)

gunluk("merhaba dünya! dosyamin ismi: ", __file__)
import discord
import os
class Ebeveyn(discord.Client):
    def __init__(self, token_ismi) -> None:
        super().__init__(intents=discord.Intents.all())
        token = os.environ.get(token_ismi)
        if token is None:
            gunluk(f"{token_ismi} degeri tanimli degil")
            exit(-1)
        self.token_ismi = token_ismi
        self.run(token)

    async def on_ready(self):
        gunluk("atis serbest", self.user)

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