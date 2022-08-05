
import discord
from alayina_gider import Cogcu
from discord.ext.commands import *
from baslayacagim_yazi import Yazi
from baslayacagim_diller import Diller

def secenekOlusturucu(secenekler: list[tuple[str, str]]):
    return discord.ui.select(
        placeholder = "Seçim yapınız.", min_values = 1, max_values = 1,
        options = [discord.SelectOption(label=x, description=y) for x, y in secenekler]
    )
async def geriCagrimOlusturucu(bot, select, interaction, siradaki):
    secim = None
    for k, v in enumerate(select.options):
        if v.value == select.values[0]:
            secim = k
            break
    if secim is None:
        bot.gunluk("sacma sapan seyler oluyor bir bakarsin")
        return
    await interaction.response.edit_message(content=f"**{siradaki[secim][1]}**", view=siradaki[secim][0]())

class Baslayacagim(Cogcu):

################################################################################

    class AkisBaslangic(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Para kazanmak için", ""),

            ("Eğlence için", ""),
            ("İlgilendiğim için", ""),
            ("Kendimi geliştirmek için", ""),

            ("Hiçbir fikrim yok, bana sadece bir dil söyle başlamak için", ""),
            ("Çocuklarım için", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Baslayacagim.AkisParaKazanmak, "İş arayıp iş sahibi olarak mı yoksa bir fikir üzerinden mi?"),

                Yol.FikrinVarMi,
                Yol.FikrinVarMi,
                Yol.FikrinVarMi,

                (Diller.Python, "Python ile temel öğrenip yazılıma devam edebilirsiniz."),
                (Diller.Python, "Sıfırdan başlayıp Python öğrenin."),
            ])
            
    class AkisParaKazanmak(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("İş bulmak için", ""),
            ("Startup fikrim var", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Baslayacagim.IsBulmak, "Hangi alanda?"),
                Yol.Startup
            ])

    class IsBulmak(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Büyük teknoloji firmaları ile çalışmak istiyorum", ""),
            ("Farketmez sadece parayla ilgileniyorum", ""),
            ("Web uygulama geliştirme", ""),
            ("Kurumsal uygulama geliştirme", ""),
            ("Mobil uygulama geliştirme", ""),
            ("3D Oyun geliştirme", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Baslayacagim.BuyukFirmalar, "Hangi firma?"),
                (Diller.Java, Yazi.Sonuc),
                (Baslayacagim.WebIsBulmak, "Hangi web alanında?"),
                Yol.Kurumsal,
                Yol.Mobil,
                (Diller.Cpp, Yazi.Sonuc),
            ])

    class BuyukFirmalar(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Facebook/Meta", ""),
            ("Apple", ""),
            ("Microsoft", ""),
            ("Google", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Python, Yazi.Sonuc),
                (Diller.Swift, Yazi.Sonuc),
                (Diller.Csharp, Yazi.Sonuc),
                (Diller.Python, Yazi.Sonuc),
            ])

    class Startup(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("3D Oyun geliştirme", ""),
            ("Mobil uygulama geliştirme", ""),
            ("Kurumsal uygulama geliştirme", ""),
            ("Web uygulama geliştirme", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Cpp, Yazi.Sonuc),
                Yol.Mobil,
                Yol.Kurumsal,
                (Baslayacagim.WebStartup, "Fikriniz gerçek zamanlı veri işliyor mu (twitter gibi)?"),
            ])
            
    class WebStartup(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Evet", ""),
            ("Hayır", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Javascript, Yazi.Sonuc),
                Yol.YuksekPotansiyel
            ])

    class MobilUygulama(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("iOS", ""),
            ("Android", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Swift, Yazi.Sonuc),
                (Diller.Java, Yazi.Sonuc),
            ])

    class Kurumsal(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Microsoft tutkunuyum", ""),
            ("Eh işte öyle böyle", ""),
            ("Benden uzak olsun", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Csharp, Yazi.Sonuc),
                (Diller.Java, Yazi.Sonuc),
                (Diller.Java, Yazi.Sonuc),
            ])

    class WebIsBulmak(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Front-end", "Tasarımla karışık yazılım gibi düşünebilirsiniz."),
            ("Back-end", "Webin beyni, yazılım gibi düşünebilirsiniz."),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Javascript, Yazi.Sonuc),
                (Baslayacagim.KimeCalisacagim, "Kimle çalışmak istiyorsunuz?"),
            ])

    class KimeCalisacagim(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Kurumsal firmalar", ""),
            ("Startup firmaları", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                Yol.Kurumsal,
                Yol.YuksekPotansiyel
            ])
            
    class YuksekPotansiyel(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Evet", ""),
            ("Emin değilim", ""),
            ("Hayır", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Javascript, Yazi.Sonuc),
                Yol.FavoriOyuncak,
                Yol.FavoriOyuncak
            ])

    class FavoriOyuncak(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Lego", ""),
            ("Play-Doh", ""),
            ("Çok eski çirkin bir oyuncağım vardı fakat onu çok seviyordum", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Python, Yazi.Sonuc),
                (Diller.Ruby, Yazi.Sonuc),
                (Diller.Php, Yazi.Sonuc),
            ])

    class FikrinVarMi(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Yok. Sadece başlamak istiyorum.", ""),
            ("Evet var.", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Baslayacagim.Tercihim, "İşimi..."),
                Yol.Startup
            ])

    class Tercihim(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("...kolay yoldan yapmayı tercih ederim.", ""),
            ("...en iyi yoldan yapmayı tercih ederim.", ""),
            ("...biraz zor yoldan yapmayı tercih ederim.", ""),
            ("...ciddi anlamda en zor yoldan yapmayı tercih ederim.", "(diğer dilin özelliklerini öğrenmek gittikçe kolaylaşacaktır)"),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Python, Yazi.Sonuc),
                (Diller.Python, Yazi.Sonuc),
                (Baslayacagim.Arabam, "Düz mü otomatik vites mi?"),
                (Diller.Cpp, Yazi.Sonuc),
            ])

    class Arabam(discord.ui.View):
        def __init__(self, *items, timeout = 180, bot = None):
            super().__init__(*items, timeout=timeout)
            self.bot = bot
        @secenekOlusturucu([
            ("Otomatik", ""),
            ("Düz", ""),
        ])  
        async def select_callback(self, select, interaction):
            await geriCagrimOlusturucu(self.bot, select, interaction, [
                (Diller.Java, Yazi.Sonuc),
                (Diller.C, Yazi.Sonuc),
            ])

################################################################################

    @slash_command(description="programlamaya başlamak istiyor ve nereden başlayacağınızı bilmiyorsanız hemen bu komutu çalıştırın!")
    async def baslayacagim(self, ctx):
        await ctx.respond("**Programlamayı neden öğrenmek istiyorsunuz?**", view=__class__.AkisBaslangic(bot=self.bot), ephemeral=True)


class Yol():
    Mobil = (Baslayacagim.MobilUygulama, "Hangi ortam?")
    Kurumsal = (Baslayacagim.Kurumsal, "Microsoft hakkında ne düşünüyorsunuz?")
    YuksekPotansiyel = (Baslayacagim.YuksekPotansiyel, "Potansiyeli yüksek fakat olgunlaşmamış bir dil öğrenmek ister misiniz?")
    FavoriOyuncak = (Baslayacagim.FavoriOyuncak, "Favori oyuncağınız hangisi?")
    FikrinVarMi = (Baslayacagim.FikrinVarMi, "Aklınızda bir fikir veya platform var mı?")
    Startup = (Baslayacagim.Startup, "Hangi alanda?")

Baslayacagim("TPBOT_TOKEN_NAZGUL_1", Baslayacagim.__name__.lower())