import discord
import os
from dotenv import load_dotenv
load_dotenv()

# Enable message content intent
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'Hi {client.user} I am online.')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('#hello'):
    await message.channel.send('Hello World bitechs')

print(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))