baslat = [
    "testci1",
    "testci2",
]
githubcom = r"https://raw.githubusercontent.com/0xdeadc0de/lightweight-tpbot/main/botlar"

from threading import Thread
from importlib import import_module
import requests
import time
from botlar.alayina_gider import Cogcu, yonetici_mi
from discord.ext.commands import *

class Efendi(Cogcu):
    isciler = []

    def ise_basla(self, dosya):
        isci = Thread(target=import_module,args=[f"botlar.{dosya}"])
        isci.run()
        self.isciler.append(isci)

    @Cog.listener()
    async def on_ready(self):
        for dosya in baslat:
            self.ise_basla(dosya)
            
    @command()
    @check(yonetici_mi)
    async def paydos(self, ctx):
        fesih = 0
        toplam = len(self.isciler)
        for isci in self.isciler:
            try:
                isci.join()
                fesih += 1
            except:
                bot.gunluk("bir isci ariza cikardi. hangisi soylemem ama")
                continue
        self.isciler = []

        mesaj = f"{fesih}/{toplam} isci basariyla feshedildi."
        bot.gunluk(mesaj)
        await ctx.send(mesaj)
        return

    @command()
    @check(yonetici_mi)
    async def yukle(self, ctx, dosya):
        self.ise_basla(dosya)
        return

    @command()
    @check(yonetici_mi)
    async def github(self, ctx, dosya):
        cevap = requests.get(f"{githubcom}/{dosya}.py")
        if not cevap.ok:
            bot.gunluk("github yuklemesi basarisiz oldu. cevap: ", cevap.status_code, cevap.reason)
            return

        isim = f"gecici_{dosya}_{time.time()}"
        try:
            dosya = open(f"botlar/{isim}.py", "w", encoding="UTF8")
            dosya.write(cevap.text)
            dosya.flush()
            dosya.close()
        except:
            bot.gunluk("github yukleme sonrasi dosya olusturma basarisiz oldu. gecmis olsun. error code falan yok sana. git soguk su ic.")
            return

        self.ise_basla(isim)

Efendi("TPBOT_TOKEN_KARANLIKLAR_LORDU", Efendi.__name__)