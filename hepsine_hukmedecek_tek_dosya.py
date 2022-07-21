baslat = [
    "onayci"
]
githubcom = r"https://raw.githubusercontent.com/0xdeadc0de/lightweight-tpbot/main/botlar"
py = "python"

from botlar.alayina_gider import Tpbot, yonetici_mi
from discord.ext.commands import *
bot = Tpbot("TPBOT_TOKEN_KARANLIKLAR_LORDU")

isciler = []
import subprocess
def ise_basla(dosya):
    isci = subprocess.Popen([py, dosya])
    isciler.append(isci)

@bot.listen()
async def on_ready():
    for dosya in baslat:
        ise_basla(f"botlar/{dosya}.py")


import requests
@bot.command()
@check(yonetici_mi)
async def paydos(ctx):
    global isciler
    fesih = 0
    toplam = len(isciler)
    for isci in isciler:
        try:
            isci.terminate()
            fesih += 1
        except:
            bot.gunluk("bir isci ariza cikardi. hangisi soylemem ama")
            continue
    isciler = []

    mesaj = f"{fesih}/{toplam} isci basariyla feshedildi."
    bot.gunluk(mesaj)
    await ctx.send(mesaj)
    return

@bot.command()
@check(yonetici_mi)
async def yukle(ctx, dosya):
    ise_basla(f"botlar/{dosya}.py")
    return

import requests
import time
@bot.command()
@check(yonetici_mi)
async def github(ctx, dosya):
    cevap = requests.get(f"{githubcom}/{dosya}.py")
    if not cevap.ok:
        bot.gunluk("github yuklemesi basarisiz oldu. cevap: ", cevap.status_code, cevap.reason)
        return

    isim = f"gecici_{dosya}_{time.time()}.py"
    try:
        dosya = open(isim, "w", encoding="UTF8")
        dosya.write(cevap.text)
        dosya.flush()
        dosya.close()
    except:
        bot.gunluk("github yukleme sonrasi dosya olusturma basarisiz oldu. gecmis olsun. error code falan yok sana. git soguk su ic.")
        return

    ise_basla(isim)

bot.baslat()