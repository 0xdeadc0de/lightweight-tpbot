yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]
token_ismi = "TPBOT_TOKEN_KARANLIKLAR_LORDU"

import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user, f"[{token_ismi}]")

    async def on_message(self, message):
        
        if message.author == self.user or\
           message.author.id not in yoneticiler:
            return
        print(message.author.id)

        if message.content == '~ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

import os
token = os.environ.get(token_ismi)
if token is None:
    print("TPBOT_TOKEN degeri tanimli degil")
    exit(-1)
client.run(token)