baslat = [
    "onayci",
    "baslikci",
    "rolcu",
    "sorucu",
    "baslayacagim",
    "kartci",
]
githubcom = r"https://raw.githubusercontent.com/0xdeadc0de/lightweight-tpbot/main/botlar"
token_ismi = "TPBOT_TOKEN_KARANLIKLAR_LORDU"

from importlib import import_module, util
import requests
import time, sys
from botlar.alayina_gider import Cogcu, thumbs, yonetici_mi, cogbotlar
from discord.ext.commands import *

class Efendi(Cogcu):
    isciler = []

    def ise_basla(self, dosya: str):
        dosya = dosya.lower()
        hedef = f"botlar.{dosya}"
        if hedef in sys.modules:
            sys.modules.pop(hedef)
        
        if not util.find_spec(hedef):
            return False
        import_module(hedef)
        return True

    @Cog.listener()
    async def on_ready(self):
        for dosya in baslat:
            self.ise_basla(dosya)
            
    @command()
    @check(yonetici_mi)
    async def paydos(self, ctx):
        fesih = 0
        toplam = len(self.isciler)
        for token, cogbot in cogbotlar.items():
            if token == token_ismi:
                continue
            try:
                await cogbot.close()
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
        await thumbs(ctx, self.ise_basla(dosya))

    @command()
    @check(yonetici_mi)
    async def github(self, ctx, dosya):
        cevap = requests.get(f"{githubcom}/{dosya}.py")
        if not cevap.ok:
            bot.gunluk("github yuklemesi basarisiz oldu. cevap: ", cevap.status_code, cevap.reason)
            return

        isim = f"gecici_{dosya}_{time.time()}".replace(".","")
        try:
            dosya = open(f"botlar/{isim}.py", "w", encoding="UTF8")
            dosya.write(cevap.text)
            dosya.flush()
            dosya.close()
        except:
            bot.gunluk("github yukleme sonrasi dosya olusturma basarisiz oldu. gecmis olsun. error code falan yok sana. git soguk su ic.")
            return

        self.ise_basla(isim)

Efendi(token_ismi, Efendi.__name__.lower())