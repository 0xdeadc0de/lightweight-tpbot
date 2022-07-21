import discord

yoneticiler = [
    824573651390562325, # Kral Risitas
    272044185689915392, # MrChuck
]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

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
token = os.environ.get("TPBOT_TOKEN")
if token is None:
    print("TPBOT_TOKEN degeri tanimli degil")
    exit(-1)
client.run(token)