
import discord
from discord.ext.commands import *
from baslayacagim_yazi import Yazi

class Diller():
    class Python(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Ent",
                description=
f"`Zorluk: {Yazi.Yildiz[1]}`\n"+
"""
Küçük hobitlere ve programlamaya yeni başlayanlara bilgisayar bilimi konularını öğretir.

Büyücülere ve araştırmacılara yardımcı olur.

Çoğunlukla başlangıç için en iyi program olarak bilinir.

Öğrenmesi kolaydır.

Araştırma, teknik ve akademik çalışmalarda; yapay zeka gibi başlıklarda yoğun olarak kullanılır.

Django(python dili ile) kullanarak websitesi yapabilirsiniz.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[4]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="YouTube, Instagram, Spotify",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/WtuAk9U.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)

    class Java(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Gandalf",
                description=
f"`Zorluk: {Yazi.Yildiz[3]}`\n"+
"""
Barış ve huzur ister, herkes için her platformda çalışabilir.

Tüm platformlarda çalışabilmesi ile popülerdir.

En çok eleman aranan ve maaşı yüksek olan programlama dillerindendir.

Sloganı bir kere yaz ve her yerde çalıştırdır.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[4]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="Gmail, Minecraft, Çoğu Android uygulaması",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/Lm1IOKa.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)
            
    class Cpp(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Saruman",
                description=
f"`Zorluk: {Yazi.Yildiz[5]}`\n"+
"""
Herkes Saruman'ın iyi birisi olduğunu düşünür.

Fakat onu tanımaya başladığınızda, iyilikten ziyade güce olan tutkusunu farkedersiniz.

C dilinin daha karmaşık ve üzerine yeni özellikler eklenmiş türevidir.

Oyun geliştirmede, endüstriyel ve kritik performans gerektiren alanlarda yaygın olarak kullanılır.

Cpp dilini öğrenmek, bir arabanın üretilip parçalarının tek tek nasıl bir araya geldiğini öğrenmek gibidir.

Bir rehber, hocanız veya mentorunuz varsa öğrenilmesi tavsiye edilir.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[3]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="İşletim sistemleri, donanım ve tarayıcılar",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/Pgj27Gs.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)
            
    class Swift(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Smaug",
                description=
f"`Zorluk: {Yazi.Yildiz[3]}`\n"+
"""
Altını seven yanlız ejderha.

MacOS X ve iOS ortamlarında Apple cihazlarına uygulama geliştirmek için kullanılır.

Sadece bu ortamlarda geliştirme yapmak istiyorsanız öğrenilmesi tavsiye edilir.

Objective-C dili bu dilin arkada bıraktığı eski dildir. (Swift daha yenidir)
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[2]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="Çoğu MacOS X ve iOS uygulamaları",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/hKyKHe5.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)
              
    class Csharp(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Elf",
                description=
f"`Zorluk: {Yazi.Yildiz[3]}`\n"+
"""
Rivendell diyarlarından çıkmayıp Microsoft ortamında geliştirme ile kendini limitleyen bu güzel varlıklar yakın zamanda bir çok platforma açıldı.

dotNET Core ile birçok ortama geliştirme yapılabilmektedir.

ASP.NET kullanılarak websitesi yapılabilir.

Yazımı (syntax) ve özellikleriyle Java diline çok benzerdir.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[4]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="Kurumsal ve Windows uygulamaları",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/DrVZteT.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)

    class Javascript(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Hobbit",
                description=
f"`Zorluk: {Yazi.Yildiz[2]}`\n"+
"""
Çoğunlukla küçümsenen güçlü varlıklar.

Shire'ın sakin yavaş bir hayatı ile tanınırlar. Tarayıcıların yavaşlığı gibi.

En popüler web scripting dilidir.

Nodejs ile birlikte çok güçlü bir masaüstü ve backend desteği vardır.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[5]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="PayPal, Discord, çoğu sitelerin ön yüzü (front-end)",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/g93j7lj.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)
            
    class Ruby(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" İnsan",
                description=
f"`Zorluk: {Yazi.Yildiz[2]}`\n"+
"""
Çok duygusal varlıklardır.

Ruby geliştiricileri Orta Dünya'ya hükmetmesi gerektiklerini düşünürler ve kendilerini üstün hissederler.

Websiteleri ile ünlüdür.

İşi bitirmeye odaklı bir dildir.

Eğlenceli ve üretken bir kodlama deneyimi için geliştirilmiştir.

Eğlence, kişisel projeler, startup ve hızlı geliştirme için birebirdir.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[3]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="Hulu, Groupon, Slideshare",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/vk7qKh6.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)
            
    class Php(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" Ork",
                description=
f"`Zorluk: {Yazi.Yildiz[2]}`\n"+
"""
Çirkin bir görünüş, kurallara uymaz ve öngörülemezdir.

Bakımını yapan geliştiriciler için bir baş ağrısıdır.

Buna rağmen webin en popüler dilidir (Zamanında çok fazla websitesi geliştirilmiştir)

Kısa zamanda küçük website geliştirmek için uygundur.

Nerdeyse tüm web hosting firmaları tarafından düşük ücretle desteklenmektedir.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[3]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="Wordpress, Wikipedia, Flickr",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/U5bWF9E.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)

    class C(discord.ui.View):    
        @discord.ui.button(label=__qualname__[7:]+Yazi.Kesfet, style=discord.ButtonStyle.success, emoji=Yazi.KesfetEmoji) 
        async def button_callback(self, button, interaction):
            embed = discord.Embed(
                title=__class__.__name__+" dili Güç yüzüğü",
                description=
f"`Zorluk: {Yazi.Yildiz[4]}`\n"+
"""
Tek yüzüğün gücü herkes tarafından bilinir.

Herkes bu güce sahip olmak ister.

Programlama dillerinin de-fakto standartıdır.

Dünya çapında bilinen eski ve yaygın kullanılmış bir dildir.

Sistem ve donanım programlamada popülerdir.

Birkaç detay dışında C++ diliyle uyumludur. C++'in babasıdır.
""",
                fields=[
                    discord.EmbedField(name=Yazi.Populerlik,value=f"`{Yazi.Yildiz[4]}`",inline=True),
                    discord.EmbedField(name=Yazi.Yapiminda,value="Wordpress, Wikipedia, Flickr",inline=True),
                ]
            )
            embed.set_thumbnail(url="https://i.imgur.com/jK7Pf55.png")
            await interaction.response.edit_message(view=None, content=Yazi.KartBaslik, embed=embed)