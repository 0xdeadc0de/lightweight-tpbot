token_ismi = "TPBOT_TOKEN_NAZGUL_1"
py = "python"
izinli_roller = [
    801135743229624320, #KURUCU
    830478022183616564, #EDITOR
    826741535839748096, #ASISTAN
]

import time
def gunluk(*mesajlar):
    print(time.strftime("%Y/%m/%d %H:%M (GMT%z)"), f"[{token_ismi}]:", *mesajlar)

gunluk("merhaba dünya")
import discord
class MyClient(discord.Client):

    async def on_ready(self):
        gunluk("atis serbest", self.user)

    async def on_message(self, message: discord.Message):
        
        # kullanicinin sahip oldugu tum rollerden birisi bile izinli rolde yoksa cikis yap
        if message.author == self.user or all(x.id not in izinli_roller for x in message.author.roles):
            return

        # bu noktadan sonra sadece izinli roller
        if message.content.startswith("!onay "):
            if len(message.mentions) > 0:
                try:
                    uye: discord.member.Member = message.mentions[0]
                    
                    tp_uyesi_rolu = discord.utils.get(uye.guild.roles, id=900647464342790204)
                    await uye.add_roles(tp_uyesi_rolu)
                
                    await message.add_reaction('\N{THUMBS UP SIGN}')
                except:
                    await message.add_reaction('\N{THUMBS DOWN SIGN}')
            else:
                await message.add_reaction('\N{THUMBS DOWN SIGN}')
            await message.delete(delay=5)
        


intents = discord.Intents.default()
client = MyClient(intents=intents)

import os
token = os.environ.get(token_ismi)
if token is None:
    gunluk(f"{token_ismi} degeri tanimli degil")
    exit(-1)
client.run(token)