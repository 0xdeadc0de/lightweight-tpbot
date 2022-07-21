yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
token_ismi = "TPBOT_TOKEN_TEST"

print(f"[{token_ismi}]", "merhaba dünya")
import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"[{token_ismi}]", 'Atis serbest', self.user)

    async def on_message(self, message):
        
        if message.author == self.user or\
           message.author.id not in yoneticiler:
            return

        if message.content == '!ping':
            await message.channel.send(f'pong [{token_ismi}]')
            
        if message.content.startswith("!kapan "):
            hedef = message.content[7:]

            if hedef == token_ismi:
                exit(1)
            return

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

import os
token = os.environ.get(token_ismi)
if token is None:
    print(f"[{token_ismi}]", f"{token_ismi} degeri tanimli degil")
    exit(-1)
client.run(token)