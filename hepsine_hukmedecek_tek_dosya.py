yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
token_ismi = "TPBOT_TOKEN_KARANLIKLAR_LORDU"
github = r"https://raw.githubusercontent.com/0xdeadc0de/lightweight-tpbot/main/botlar"

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
            subprocess.Popen(["py", f"botlar/{dosya}.py"])
            return

        if message.content.startswith("!github "):
            dosya = message.content[8:]

            cevap = requests.get(f"{github}/{dosya}.py")
            if not cevap.ok:
                gunluk("github yuklemesi basarisiz oldu. cevap: ", cevap.status_code, cevap.reason)
                return

            isim = f"gecici_{dosya}_{time.time()}.py"
            try:
                dosya = open(isim, "w", encoding="UTF8")
                dosya.write(cevap.text)
                dosya.flush()
                dosya.close()
            except:
                gunluk("github yukleme sonrasi dosya olusturma basarisiz oldu. Gecmis olsun. Error code falan yok sana. Git soguk su ic.")
                return

            subprocess.Popen(["py", isim])
            return

intents = discord.Intents.default()
client = MyClient(intents=intents)

import os
token = os.environ.get(token_ismi)
if token is None:
    gunluk(f"{token_ismi} degeri tanimli degil")
    exit(-1)
client.run(token)