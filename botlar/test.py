from alayina_gider import Ebeveyn, yoneticiler
class Testci(Ebeveyn):
    async def on_message(self, message):
        await super(self, message)

        if message.author == self.user or\
           message.author.id not in yoneticiler:
            return

        if message.content.startswith("!kapan test"):
            exit(1)

Testci("TPBOT_TOKEN_TEST")