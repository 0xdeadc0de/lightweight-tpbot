baslat = [
    "onayci"
]
github = r"https://raw.githubusercontent.com/0xdeadc0de/lightweight-tpbot/main/botlar"
py = "python"

import requests
import subprocess
from alayina_gider import gunluk, Ebeveyn, yoneticiler
class KaranliklarEfendisi(Ebeveyn):
    isciler = []

    def baslat(self, dosya):
        isci = subprocess.Popen([py, dosya])
        self.isciler.append(isci)


    async def on_ready(self):
        super(self)

        for dosya in baslat:
            self.baslat(f"botlar/{dosya}.py")

    async def on_message(self, message):
        super(self, message)
        
        if message.author == self.user or\
           message.author.id not in yoneticiler:
            return

        if message.content == "!paydos":
            fesih = 0
            toplam = len(self.isciler)
            for isci in self.isciler:
                try:
                    isci.terminate()
                    fesih += 1
                except:
                    gunluk("bir isci ariza cikardi. hangisi soylemem ama")
                    continue
            self.isciler = []

            mesaj = f"{fesih}/{toplam} isci basariyla feshedildi."
            gunluk(mesaj)
            await message.channel.send(mesaj)
            return
        
        if message.content.startswith("!yukle "):
            dosya = message.content[7:]
            self.baslat(f"botlar/{dosya}.py")
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

            self.baslat(isim)
            return

KaranliklarEfendisi("TPBOT_TOKEN_KARANLIKLAR_LORDU")