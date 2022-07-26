from kartci_nitelik import CardPlayKind, CardRarity, CardTitle
class CardText():
    def __init__(self, baslik, cins, aciklama, link, kombo=[]) -> None:
        self.aciklama = aciklama
        self.baslik = baslik
        self.cins = cins
        self.link = link
        self.kombo = kombo

kartlar = [
    # 1
    CardText(CardTitle["Efsanevi Atatürk"],
        CardRarity.Destansı,
        "Oyuncuyu tum zararli buyulerden kurtarir, gucunu tamamen yeniler ve dusmanin tum yararli buyulerini bozar.",
        "https://media1.tenor.com/images/2f94086d9d8d7616090e8dabb8e17ff7/tenor.gif?itemid=15462494"
    ),
    
    # 2
    CardText(CardTitle["Şakasına gülünmeyen adam"],
        CardRarity.Esrarengiz,
        "Hoca komik bir laz fikrasi anlatir ve dusman bir tur boyunca afallar",
        "https://media1.tenor.com/images/726bfd542c9483c0831bbef0b658d978/tenor.gif"
    ),
    CardText(CardTitle["Muzlu Ajdar"],
        CardRarity.Güzide,
        "Popstar Ajdar teknesinden dusmanina dogru bir bakis attiktan sonra muzundan bir isirik alir. Dusman kendini Turkiye'nin stari karsisinda gucsuz hisseder.",
        "https://media1.tenor.com/images/ef02df106010033ce4edc91c3a602308/tenor.gif?itemid=15700432"
    ),
    CardText(CardTitle["Koca isteyen kari"],
        CardRarity.Güzide,
        "Koca isteyen kari polislerin elinde rehin durumdadir ve Oyuncu yazi tura atar. Yazi gelmesi halinde Koca isteyen kari polislerin elinden bir hazimle kurtularak oyuncuyu zararli buyulerden defeder. Bu durumda Oyuncu bir daha yazi tura atar. Eger tekrar yazi gelirse Koca isteyen kari dusmanina aldigi depar sonucu kafa atar ve ona X hasar verir",
        "https://media1.tenor.com/images/34121fc8c9f07be8fc19a13f300df98f/tenor.gif?itemid=11898048"
    ),

    # 5
    CardText(CardTitle["KorkusuzBöyle"],
        CardRarity.İhtişamlı,
        "Korkusuz Korkak dusmanini tokat yagmuruna tutar. Oyuncu en fazla bes kere ard arda yazi tura atar. Her gelen yazi icin dusmani 20 saglik kaybeder. Ilk gelen tura ardindan yazi tura atma kesilir.",
        "https://media1.tenor.com/images/b93b5c2d5566ff7420f53679cfa49ac3/tenor.gif?itemid=12492940"
    ),
    CardText(CardTitle["Kara Murat benim"],
        CardRarity.Esrarengiz,
        "Kara Murat 2 tane klon kardeşini oluşturup kara murat benim diye haykırır ve sesi aynı anda echo yapar. Kara murat kardeşleriyle sağ gösterip sol vurur. Rakip gerçek Kara Murat tarafından 10 hasar alır. Klon kardeşleri yazı atarsa düşmana 10 hasar verir.",
        "https://media.tenor.com/images/fad02d9f6cf14dd6dd116f3739d55b4b/tenor.gif"
    ),
    CardText(CardTitle["Yossi Kohen"],
        CardRarity.İhtişamlı,
        "Yahudi is adami Yossi Kohen cok fazla guler ve bunun sonucunda dusman yapmis oldugu saldirinin aynisini kendi hanesine uygular. Ayni zamanda Yossi Kohen firsat buldukca duzenli tras oldugu icin dusmanin uzerinde bulunan iyilestirmelerden Oyuncu ayni sekilde faydalanir",
        "https://i.imgur.com/tauumAv.png"
    ),
    CardText(CardTitle["8 Top"],
        CardRarity.Yaygın,
        "",
        "https://media.tenor.com/images/904da7243ad3d7dfd5c553b48b374d0b/tenor.gif"
    ),
    CardText(CardTitle["Zikir halkası"],
        CardRarity.Esrarengiz,
        "Oyuncu elindeki tum kartlari desteye geri koyar, kartlari karistitir ve tekrar ayni miktarda kart geri ceker.",
        "https://media1.tenor.com/images/a5841e7db62735c0c85b6c6ddf670afe/tenor.gif?itemid=18466605"
    ),

    # 10
    CardText(CardTitle["Erotik Ajdar"],
        CardRarity.İhtişamlı,
        "Popstar Ajdar bir esinti edasi ile dans etmeye baslar. Erotik figurleri karsisinda gozleri kamasmis olan dusmanin elinden tum kartlari masaya acilir ve gizli emelleri apacik ortaya tezahur eder.",
        "https://media1.tenor.com/images/dc1947baee381b7b23a02d6a6b4596d3/tenor.gif?itemid=15700431"
    ),
    CardText(CardTitle["Yengec Risitas"],
        CardRarity.İhtişamlı,
        "Oyuncunun yaninda destek olmak icin Yengec Risitas ringe cikar ve saldirgan bir sekilde yengec dansi yapmaya baslar. Rakip kendi sirasi bitiminde yazi tura atar. Yazi gelirse Risitas knock-out olur ancak tura gelirse Risitas kiskaclariyla rakibe 20 hasar verir ve hayatta kalmaya devam eder.",
        "https://media1.tenor.com/images/0ac10f80d848a929d272edcff0acb9a4/tenor.gif?itemid=19258334"
    ),
    CardText(CardTitle["Gözleri kayan Acun"],
        CardRarity.İhtişamlı,
        "Oyuncu medya sahibi Acun'u sahaya davet eder ve rakip bir sonraki tur yapacagi darbe Acun'a isabet eder. Acunun gozleri kayar. Oyuncu hasar almaz.",
        "https://media.tenor.com/images/02c2e5da032abca1e18228c759c7a895/tenor.gif"
    ),
    CardText(CardTitle["Halay"],
        CardRarity.Güzide,
        "Oyuncu halaya dahil olur ve oynamaya baslar. Halay sirasinda halay basi yazi tura atar. Eger yazi gelirse Oyuncu destesinden istedigi bir karti alir.",
        "https://media.tenor.com/images/9f3d15280ecb7c20d4c6d3d35a52ce26/tenor.gif"
    ),
    CardText(CardTitle["Tivorlu İsmail"],
        CardRarity.Esrarengiz,
        "Tivorlu Ismail Hela Vela Velvela adli eserini canlandirmaya baslar. Hay Masallah dedikten sonra Zih der ve Aaaa diye yukselmeye baslar. Rakip 20 hasar alir. Tivorlu Ismail Aaaaa nakaratini tekrarladikca oyuncu yazi tura atar. Her yazi ardina tekrar yazi tura atar ve rakibine 10 hasar verir. Oyuncu yazi turayi 3 kere kombolama hakkinda sahiptir. Eger oyuncu 3 kere yazi tutturursa Ismail Hay masallah diyip parcasini bitirir ve Oyuncu kendine 20 hasar verir.",
        "https://media3.giphy.com/media/wHshvtykRrWps6mRd9/giphy.gif?cid=790b7611188bc1540c6cf34302e94666ad4e84a640e886b5&rid=giphy.gif&ct=g"
    ),

    # 15
    CardText(CardTitle["ChangerBöyle"],
        CardRarity.Destansı,
        "Karsi rakibin herhangi bir kartini taklit edebilir.",
        "https://i.imgur.com/zdpOsfj.png"
    ),
    CardText(CardTitle["Tatar Ramazan"],
        CardRarity.Esrarengiz,
        "Yazi tura at. Yazi gelirse dusmana 40 hasar yapistir.",
        "https://i.imgur.com/Cphcq5a.png"
    ),
    CardText(CardTitle["TP Moderatörlerin gazabı"],
        CardRarity.Destansı,
        "TP Discord sunucusunu moderatörleri bir araya gelerek üyeler üzerinde yetkilerini kullanma suretiyle sunucuda terör estirmeye başlarlar. Korku içerisinde kalan rakip ne yapamayacağını bilemez ve 2 tur boyunca oyundan banlanır, kart çekemez.",
        "https://media3.giphy.com/media/XaLLCvwgRxpwlnnzkh/giphy.gif?cid=790b7611438c6d6c0cfddbdb168cc8b86b99d49cac4b7a29&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Inshallah"],
        CardRarity.Güzide,
        "Türk programcı yazılım geliştirme yaparken takıldığı noktaları ve sorunları TP Discord sunucusunda paylaşır. Sunucu bireyleri oyuncuya destek olarak sorununu çözer, yardımcı olur ve inşallah gifi atarlar. Bunun sonunda motive olmuş üye kod yazmaya devam eder ve iki tur boyunca 20 iyileştirme alır.",
        "https://c.tenor.com/wnuXIUDfJLsAAAAC/ron-swanson-nick-offerman.gif"
    ),
    CardText(CardTitle["Le Umut Peace"],
        CardRarity.Esrarengiz,
        "Sunucuda Umut sohbetin tam ortasında durduk yere peace gifi atar ve ortadan kaybolur. Bunun sonucunda sunucu üyeleri afallar ve rakip 1 el boyunca hedefini ortada bulamaz.",
        "https://c.tenor.com/xjz_SE0yqXQAAAAC/peace-disappear.gif"
    ),

    # 20
    CardText(CardTitle["Kralın Soytarı gifi"],
        CardRarity.İhtişamlı,
        "TP Kralı sunucuda Umutun peace gifi üzerine Soytarı Peace gifi atar. Oyuncu ortadan kaybolur ve rakip 1 el boyunca hedefini ortada bulamaz. Eğer herhangi bir oyuncu önceden Le Umut Peace kartı atmışsa bunun üzerine oynanan bu kart kombo etkisi yaratır ve ansızın modsuz kalan sunucuda kaos ortamı oluşur. İki oyuncu rastgele birer kart kaybeder ve 20 hasar puanı alırlar.",
        "https://c.tenor.com/a5d4lrIx9rIAAAAd/jimin-bye-jimin-bts.gif"
    ),
    CardText(CardTitle["Küfürbaz Kral"],
        CardRarity.Destansı,
        "TP Kralı sunucudan uzun bir süre uzakta kalır ve geri geldiğinde notification fırtınasına uğrar. Bunun sonucunda sinirlenir ve notification sayısı kadar düşmana hasar verir. Bu saldırı koruyucu büyüler tarafından engellenemez.",
        "https://media.giphy.com/media/PL4yLaVxeYreemo2kY/giphy.gif"
    ),
    CardText(CardTitle["Tempolu Günaydın"],
        CardRarity.Esrarengiz,
        "Oyuncu güne iyi başlar ve her round başı yazı tura atar. Yazı gelmesi durumunda tur başı çektiği kartın üzerine fazla bir kart çeker. Bu büyü uç tur sürer.",
        "https://c.tenor.com/_1z9JvYh7dwAAAAC/goose-silly.gif"
    ),
    CardText(CardTitle[":IBOY:"],
        CardRarity.Güzide,
        "Oyuncu TP sunucusunda en çok kullanılan emojiyi atar 1 kart çeker ve rakip 10 hasar alır. Oyuncu :IBOY: kartını ard ardına spamlaması durumunda her bir oynayış başı kartın hasarı 10 artar. Kart en fazla 30 hasara ulaşabilir.",
        "https://i.imgur.com/uJf8aiE.png"
    ),
    CardText(CardTitle["HainBöyle"],
        CardRarity.Destansı,
        "RabirtBoyle TP Discord sunucunun sahibi olmak için hain planlar yapar ve bu emeller içinde oyuncuya aynı tur içerisinde ikinci bir saldırı kartı oynama ayrıcalığı verir.",
        "https://c.tenor.com/Rbfv2Nbq_u4AAAAC/swinging-chilling.gif"
    ),

    # 25
    CardText(CardTitle["İnş cnm ya :)"],
        CardRarity.Güzide,
        "Belirsizliğin ortasında kalınıldığında sunucuda inş cnm ya gifi atılır. Ne olacağı belli olmayan bu durumda sorun yaşayan oyuncu ya 30 sağlık puanı kaybeder yada rakibine 30 hasar verir.",
        "https://media4.giphy.com/media/ob44JUxIej8jJEeEgp/giphy.gif?cid=790b7611a4c4375931ff92ee0e899e0c390702526109de29&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Moderatör Savar"],
        CardRarity.Esrarengiz,
        "Fikir geliştirmeye açık kart: Anti Mod karti veya filmin orjinal içeriğiyle alakalı bir isim",
        "https://c.tenor.com/4PY3dHdVCSoAAAAd/mute-ban.gif"
    ),
    CardText(CardTitle["Toxic Moderatör"],
        CardRarity.İhtişamlı,
        "TP sunucusunda uzun zaman geçirdikten sonra ortama alışan üye Krala istekte bulunur ve moderatör makamına erişme şerefine ulaşır. Moderatör olan oyuncu her kanalda şanlı bir yürüyüş yapar. Tüm sunucularda ünü duyulur ve karizmasının getirisiyle rakip oyuncu üye sayısının dörtte birini kaybeder, ve oyuncu bu üyeleri kendi sunucusuna transfer eder",
        "https://c.tenor.com/DrspgsurIyEAAAAd/discord-mod-discord.gif"
    ),
    CardText(CardTitle["Le Bumlugi'nin geri dönüşü"],
        CardRarity.Güzide,
        "Uzun yıllardan sonra Le Bimlugi programcılık becerilerini güçlendirip bunun yanında Rusça bilgilerinide güçlendirmiş ve Tp Krallığı topraklarına yeniden ayak basmıştır. Le Bimlugi Rusça bir kelime söyler, ne dediğini anlamayan rakip Google Translate açar, bu sırada Le Bimlugi modların dalgınlığını kullanır ve rakibine hasar verir. ",
        "https://thumbs.gfycat.com/FastImaginativeIchthyostega-size_restricted.gif"
    ),
    CardText(CardTitle["Kobra Murat"],
        CardRarity.Esrarengiz,
        "Kobra murat, üzerindeki parıltılı kıyafetleri ile göbek atmaya başlar ve rakip oyuncunun gözlerini kamaştırır. Kobra Murat oyuncudan bir kart çalar ve dans etmeyi bırakır. Eğer yakalanırsa rakip oyuncu,kart sahibinden 1 kart alır. Murat yakalanmadan kartı çalabilirse, canı 10 artar ve kart oyuncunun olur.",
        "https://c.tenor.com/OJGdPKzNtAgAAAAd/kobra-murat-roman.gif"
    ),

    # 30
    CardText(CardTitle["Kage-Bunshin No Umut"],
        CardRarity.Güzide,
        "Umut sunucudaki üyeleri kralın kılığına bürünmeye teşvik eder. Kral suncuya girdiğinde kafası karışır ve Umut'u banlamak için inşallah diyerek ban hammerini sallar ama yanlışlıkla kendisini banlar. Bunu fırsat bilen HainBöyle yönetimi devralır ve bu aşamdan sonra iki taraf içinde Bimlugi kartları etkisiz hale gelir",
        "https://media4.giphy.com/media/i3IUvUfLFi6Wz1Vjg4/giphy.gif?cid=790b76115cbf3f677a6c30e615022876d7fa575d76277ed9&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Osbir"],
        CardRarity.Esrarengiz,
        "Rakip bir şaka yapar, ceza olarak bir şuku alır ve şakacı lakabı takılır. ",
        "https://c.tenor.com/a17JuEkdmBoAAAAC/31-vegeta-laugh.gif"
    ),
    CardText(CardTitle["Hediye kart"],
        CardRarity.Yaygın,
        "Sunucu içerisinde başkasına hediye edilebilen kart. Oynandığında ise oyuncunun destesine rastgele yeni bir kart eklenir.",
        "https://c.tenor.com/_lud-QP6FQgAAAAd/other-logo.gif"
    ),
    CardText(CardTitle["PoTaToBeaTeR'ın Baskını"],
        CardRarity.Güzide,
        "Le Bimlugi Tp Krallığında sakin ve düzgün bir hayat yaşıyordu. Lakin bir gün Le Bimlugi'nin kuzeni Le Bimlugiyi kendisine yoldaş yapar ve PoTaToBeaTeR Raidini planlarlar. Tp Krallığına Raid atarlar ve uzun bir çatışma sonucunda Tp Modları yıpranır lakin buna rağmen Raid durdurulur ve Le Bimlugi ile Kuzeni Tp Krallığı topraklarından uzaklaştırılır.",
        "https://thumbs.gfycat.com/RemoteDescriptiveAngora-size_restricted.gif"
    ),
    CardText(CardTitle["Fatih'ın geri dönüşü"],
        CardRarity.Güzide,
        "Tp krallığından süresiz olarak sürülmüş olan Fatih geri dönmüştür. Kendini yazılım alanında geliştirmiş. Ütopik fikirlere sahip olmuştur.",
        "https://media2.giphy.com/media/WoHZAOgQCD2PqbqtT2/giphy.gif?cid=790b76111a528b8ad35eaccbb8bb7627fbf57906fac16efb&rid=giphy.gif&ct=g"
    ),

    # 35
    CardText(CardTitle[":TEA:"],
        CardRarity.Yaygın,
        "Oyuncu tea kartını oynadığında sohbetin ortasına peace gifi spawnlanır ve iki tarafta çay molasına çıkar. Oyuncu ve rakibi 20 sağlık kazanır.",
        "https://c.tenor.com/5_R9v9HpTE0AAAAC/tea-coffee.gif"
    ),
    CardText(CardTitle["ParantezliBöyle"],
        CardRarity.Esrarengiz,
        "RabırtBöyle yeni parantezli nickiyle sunucu hakkında bilgi toplar. Böylece rakibin elinde kaç adet saldırı kartı olduğunu öğrenir.",
        "https://media2.giphy.com/media/sGw78q7BerBHTPqnji/giphy.gif?cid=790b76118a0d39c5dad4313184170b206987881d546e6da3&rid=giphy.gif&ct=g",
        ["Oyuncu aynı kartı üst üste oynadığında RabırtBöyle .server komutunu çalıştırarak sunucu hakkındaki tüm bilgiye ulaşır ve rakibin elindeki kartları apaçık görebilir."]
    ),
    CardText(CardTitle["Kral bump"],
        CardRarity.Yaygın,
        "Kral Risitas süreye dikkat etmeden bump komutu dener. Oyuncu iki kere ardı ardına yazı atarsa Kral bump girişimi başarılı olur ve sunucu bumplanır, oyuncu 20 sağlık puanı kazanır",
        "https://media0.giphy.com/media/PvrH91rqSJvsEamllE/giphy.gif?cid=790b7611e75977c7dd45893f43ff35169a4835ae682a74b4&rid=giphy.gif&ct=g",
        ["Oyuncu ilk denemede başarısız olur ve bir daha aynı kartı oynarsa kart gücünü elde etmek için bir yazı atması yeterli olur.",
         "Oyuncu ikinci denemede başarısız olur ve bir daha aynı kartı oynarsa kart gücü direkt elde edilir ve kombo durumu sıfırlanır."]
    ),
    CardText(CardTitle["MrChuck'ın Susturucu Botu"],
        CardRarity.Esrarengiz,
        "MrChuck ModBot üzerinde susturma modülü geliştirir ve bunun sonucunda sunucuda şukusu bulunan üyeler 1 dakika boyunca sessizlik cezası yerler. ",
        "https://media0.giphy.com/media/0S8eXRkziKKc9GPlcw/giphy.gif?cid=790b7611d9d922454dcc3cc4ce657244c2470bd0afa007db&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Şuku"],
        CardRarity.Yaygın,
        "Sunucuda kurallara uymayan üyeler şukusunu alırlar. Bir şukusu bulunan üye kurallara uymamaya devam etmesi halinde ikinci bir şuku alır ve ağır uyarılırlar. En sonunda üçüncu şuku yerine gözaltına alınıp şukuları temizlenir. Gözaltına girmiş olan oyuncu tüm kartlarını kaybeder.",
        "https://c.tenor.com/bufeGeJgDLUAAAAC/candy-mae-muller.gif"
    ),

    # 40
    CardText(CardTitle["Bir bak buraya"],
        CardRarity.Yaygın,
        "Sunucudaki üyeler kuralları #bir-bak-buraya kanalından okurlar ve uygulamaya koyarlar. Bunun sonucunda oyuncu ödül olarak 1 kart çeker.",
        "https://c.tenor.com/tWbpabRvPG4AAAAC/idiot-lafuddyduddy.gif"
    ),
    CardText(CardTitle["Legendary İbo"],
        CardRarity.Destansı,
        "Oyuncu sunucuda mesajlaşırken chate milyonda bir görülen Legendary İbo gifi düşürmeyi dener. Bunun için İBO emojilerinden birini kullanır ve yazı tura atar. Yazı gelmesi durumunda kartın gücü aktif olur ",
        "https://media0.giphy.com/media/22WqiSGAepZaMzrypo/giphy.gif"
    ),
    CardText(CardTitle["Bırakın Lan Beni"],
        CardRarity.Güzide,
        "RabırtBöyle hainlikle suçlanır ve çevresindekileri sakince onu bırakmaları için uyarır.",
        "https://media1.giphy.com/media/dlx4BUpWZVgPrsnHGp/giphy.gif?cid=790b7611686b71661da9f0be9c0f4099fce011790ceb074d&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["@everyone"],
        CardRarity.Güzide,
        "İki oyuncu sunucuda atılan everyone etiketinden dolayı bildirim alırlar. Kartı oynayan oyuncu yeni bir kart çeker.",
        "https://media0.giphy.com/media/a62MfY4TCAnXHwo8sj/giphy.gif?cid=790b7611742fbc440854cebc082ac6bfaf4cdb773b1b0086&rid=giphy.gif&ct=s"
    ),
    CardText(CardTitle["Etiket"],
        CardRarity.Yaygın,
        "Sunucuda aktif olan iki oyuncudan biri yazı tura sonucu etiketlenir. Oyuncu tura atarsa kendine, yazı atarsa rakibine etiket atar. Kartı oynayan oyuncu yeni bir kart çeker",
        "https://c.tenor.com/V6vHhQ_A05YAAAAd/kamen-rider-kiva-otoya-kurenai.gif"
    ),

    # 45
    CardText(CardTitle["Çifte Bump"],
        CardRarity.İhtişamlı,
        "Sunucuda aktif olan iki oyuncu aynı anda bump yapar ve bump sayıları artar. Kartı oynayan oyuncu iki kart çeker",
        "https://media2.giphy.com/media/yJT5uRq7SvmtgQFRlu/giphy.gif?cid=790b7611c79cf018ac6cabac2ea0a122a4b9d9a31c075be3&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Bump!"],
        CardRarity.İhtişamlı,
        "Oyuncu sunucuda başarıyla bump yapar ve Ekselans Risitas tarafından ödüllerle kutsanır, 20 şifa puanı alır, bir kart çeker.",
        "https://media2.giphy.com/media/xIv9pltfZBXomb3yIk/giphy.gif?cid=790b76118d64d7e64642ae236c12c709b77995c375ea923a&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Ricardo Milos"],
        CardRarity.Esrarengiz,
        "Oyuncu destesinden bir kartı çekerken Ricardo ile göz göze gelir ve Ricardo gülümser, iki kart çekmesini söyler. Oyuncu Ricardo kartını oynar ve ardından iki kart çeker. ",
        "https://media2.giphy.com/media/W62wk6w0VI55Ijcnva/giphy.gif?cid=790b7611bff8340e5b25e79b3d4bb4cf177efb5725b6ba9d&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle[":IBOYD:"],
        CardRarity.Güzide,
        "Oyuncu TP sunucusunda en çok kullanılan emojinin geliştirilmiş versiyonunu atar ve :IBOY: kartını ansızın maksimum gücüne ulaştırır.",
        "https://i.imgur.com/UzJRAnZ.png"
    ),
    CardText(CardTitle["Tempolu Ördek"],
        CardRarity.Güzide,
        "Tempolü günaydınla bağlantılı birşeyler olacak",
        "https://c.tenor.com/ffMdX0JRjz8AAAAC/dance-cute-ducky-cute.gif"
    ),

    # 50
    CardText(CardTitle["Kem Gözlü Murat"],
        CardRarity.Esrarengiz,
        "Murat gözlüğünü kaldırır ve düşmanı baş döndüren kem gözü ile etkiler. Etkisi altında kalan düşman kart çeker, Kem gözlü Murat kafası dağılmış düşmanın kartını alır. Gözlüğünü geri takar ve oyuna ek kart ile devam eder.",
        "https://c.tenor.com/vXdJZ9d6LroAAAAd/kobra-murat-kobra.gif"
    ),
    CardText(CardTitle["Deli Vahit"],
        CardRarity.Güzide,
        "Deli Vahit Dönencesini seslendirmeye başlar neye uğradığını şaşıran rakip rastgele bir kart kaybeder. Oyuncu rastgele bir kart çeker. Kart kaybetme ve çekme özelliği dışında Kobra Murat kartlarına karşı kullanılırsa rakip 20 hasar alır.",
        "https://c.tenor.com/Arii6Inu9b4AAAAC/vahit.gif"
    ),
    CardText(CardTitle["Yazık kafana"],
        CardRarity.Yaygın,
        "???",
        "https://i.imgur.com/jfzKiVa.png"
    ),
    CardText(CardTitle[":YES:"],
        CardRarity.Destansı,
        "Oyuncu sunucuda sorulan C vs Cpp veya C++ vs C# gibi saçma sorulara cevap olarak YES emotu kullanır, tüm ikilemlerden kurtularak yazı mı tura mı kaygısını umursamaz, oynayacağı ilk kartın tüm özellikleri yazı gelmiş gibi davranır.",
        "https://media2.giphy.com/media/TDUEulAtsGTSGcjx27/giphy.gif?cid=790b76115cc33fcbb56439160542ad59bc09b33a8c26924b&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Ajan Simit'in Oyunu"],
        CardRarity.Yaygın,
        "Ajan Simit bot geliştirmekte olan Kral'ı oyuna getirerek sabaha kadar debug yaptırır. Basit bir hata için Kral fazlasıyla zaman harcar ve sonucunda yorulur. ",
        "https://media2.giphy.com/media/ZtHYKYJnAVBlfPdxDK/giphy.gif?cid=790b76117960f6392fc83954a8edcbafb3b5ebbd523976c0&rid=giphy.gif&ct=g"
    ),

    # 55
    CardText(CardTitle["The Lord of The Bumps"],
        CardRarity.Esrarengiz,
        "Sunucuda yapılan bumplar sayılmaya başlar. RabırtBöyle bump yağmuru yaparak sıralamada birinci olur ve Lord of the Bumps rolü alır. Bump ve çifte bump kartlari ile kombolu. Etkisi tartışmaya açık...",
        "https://media2.giphy.com/media/JQOsTq6BQ2YRLrM1ap/giphy.gif?cid=790b761115f7c7868dd4fef86f76c1e0718d0691095fc2c6&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Lütfen Komutu"],
        CardRarity.Yaygın,
        "Kadim yıllarda Admin Bot icat edilmeden önce sunucuya yeni katılan üyeler için !lutfen kullanılırdı. Bu kart kullanıldığında Kadim Ockis belirir ve MEE6 uzun bir metin gönderir. Rakip o metni okuyana dek bir tur çoktan geçmiştir.",
        "https://media0.giphy.com/media/923D63VZe7fvimXvAo/giphy.gif?cid=790b76115f52ef72197bed337a732e84508df01d1a81023e&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Yapay Zeka'lı EfsoDuyar"],
        CardRarity.Yaygın,
        "Chuck tarafından yazılan ama bununla yetinmeyip kendi zekasını oluşturan EfsoDuyar botunun kartı. Efsoduyar sunucudaki her mesajı takip eder ve konuya göre emoji göndererek herkesin aklını başından alır.",
        "https://media1.giphy.com/media/OKi6xKPvBraCQzoCSy/giphy.gif?cid=790b76110068991f3f850eb50365b2c62ed877d487b18a98&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Kadim Ockis"],
        CardRarity.Destansı,
        "Kadim yılların en güçlü kartı. Günümüzdeki etkisi bilinmemektedir ¯\_(ツ)_/¯...",
        "https://media2.giphy.com/media/N30kI0lTYmwuS0hRyO/giphy.gif?cid=790b7611bed160d97fc94c06ea7cdbc87c00a0a88d68f5f9&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Risitasa Veda"],
        CardRarity.Yaygın,
        "Risitas 28 Nisan 2020 tarihinde Hakk'ın rahmetine ulaşmıştır. Oyuncu bu kartı kullandığında rakiple beraber risitasa saygı duruşunda bulunurlar ve bir tur geçer.",
        "https://c.tenor.com/l-BK1zgqIqwAAAAC/kekbye-risitas.gif"
    ),

    # 60
    CardText(CardTitle["Cinnet-i Bump"],
        CardRarity.Yaygın,
        "Sunucuda herkes bump yapmak için çıldırır ve deliler gibi bump girişiminde bulunulur. Sadece bumpların efendisi gerçek bumpı yakalayabilir. Kart oynandığında yazı gelirse oyuncuya tura gelirse rakibine 1 bump gelir. Oyuncu ardından bir kart çeker. ",
        "https://media4.giphy.com/media/sXco29SCrqMmczgjhS/giphy.gif?cid=790b7611a6d05d9e66369e9a36bdc6a4d6aa1697540e532f&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Elit Murat"],
        CardRarity.Güzide,
        "Murat lüks altın rengi ceketini giyer ve vahşi bir şekilde seksi hareketler yapmaya başlar.Şok olan düşman,oyuncuya istediği 1 kartı verir ve oyuna canından -10 eksilerek devam eder.",
        "https://c.tenor.com/3ieAAe1G0boAAAAd/kobra-murat-kobra.gif"
    ),
    CardText(CardTitle["MİT ajanı MrChunk"],
        CardRarity.Güzide,
        "MİT ajanı MrChuck uzmanlık alanı herhangi bir konya kartı üzerinde etkilidir (öneri taslak)",
        "https://media0.giphy.com/media/VwlbYRAJktWM0LL1iu/giphy.gif?cid=790b76118572fd8000ff122eddc0108738d4b071657c029d&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Echo"],
        CardRarity.Yaygın,
        "Oyuncu bu kartı oynadığında oynadığı sunucu kanalı içerisinde bir echo mesaj gücü aktifleştirir.",
        "https://media1.giphy.com/media/wadpPRc8Tb1dkRDvsc/giphy.gif?cid=790b76119d3dee2900768aefaf5f0d0d6bf164df2741153b&rid=giphy.gif&ct=g"
    ),
    CardText(CardTitle["Kadim Echo"],
        CardRarity.Esrarengiz,
        "Kadim zaman echo gücüne tanıklık etmiş kişilerce anlatılan güce oyuncu bu kart sayesinde erişir ve anonim bir şekilde bulunduğu kanala echo mesajı atar (not: sunucu kuralları ihlalinde kim olduğunuz tespit edilebilmektedir)",
        "https://c.tenor.com/9UgExGfqauIAAAAC/stars-blue.gif"
    ),
]