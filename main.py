import discord
import os
import random

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

sapaan = [
    "Halo juga! 👋",
    "Haiii! 😆",
    "Halo, ada apa nih?",
    "Haechan hadir! ✨",
    "Hai juga, semoga harimu menyenangkan!"
]

@client.event
async def on_ready():
    print(f"Haechan aktif sebagai {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    pesan = message.content.lower()

    if (
        "halo" in pesan
        or "hai" in pesan
        or "haechan" in pesan
        or "pagi" in pesan
        or "malam" in pesan
    ):
        await message.channel.send(random.choice(sapaan))

client.run(TOKEN)
