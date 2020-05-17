import discord
import src.transform

class Gen_Client(discord.Client):

    def __init__(self,transformer):        
        self.Transformer = transformer
        super(Gen_Client,self).__init__()

    async def on_read(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        if message.author == self.user:
            # early return for messages from the bot itself
            # prevents dumb loops.
            return

        if message.content.startswith('$hello'):
            await message.channel.send('hey')

        if message.content.startswith('$transform'):
            # todo - better message parsing.
            inputs = message.content.split("$transform")
            input = inputs[1]
            response = self.Transformer.transform(input)
            await message.channel.send(response)