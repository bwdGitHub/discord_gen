import discord

class Gen_Client(discord.Client):
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