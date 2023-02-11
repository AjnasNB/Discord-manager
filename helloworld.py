
import discord

intents = discord.Intents.default()
intents.message_content = True

#client(bot)
client=discord.Client(intents=intents)


@client.event
async def on_ready():
    #functions
    general_channel= client.get_channel(your channel id)

    await general_channel.send('Hello World')

#run client in server
client.run('your discord token')
