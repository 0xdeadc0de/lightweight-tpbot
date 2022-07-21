yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
token_ismi = "TPBOT_TOKEN_KARANLIKLAR_LORDU"
klasor = r"C:\Users\Woot\Documents\GitHub\lightweight-tpbot\lightweight-tpbot\botlar"

import time
def gunluk(*mesajlar):
    print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{token_ismi}]:", *mesajlar)

gunluk("merhaba dünya")
import requests
import subprocess
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        gunluk("Atis serbest", self.user)

    async def on_message(self, message):
        
        if message.author == self.user or\
           message.author.id not in yoneticiler:
            return

        if message.content == '!ping':
            await message.channel.send(f'pong [{token_ismi}]')
            return

        if message.content.startswith("!kapan "):
            hedef = message.content[7:]

            if hedef == token_ismi:
                exit(1)
            return

        if message.content.startswith("!yukle "):
            dosya = message.content[7:]
            subprocess.Popen(["py", f"{klasor}\{dosya}.py"])
            return

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

import os
token = os.environ.get(token_ismi)
if token is None:
    gunluk(f"{token_ismi} degeri tanimli degil")
    exit(-1)
client.run(token)