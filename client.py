import discord
from discord.embeds import Embed
import tokens
from discord import Client

client = Client()

@client.event
async def on_message(message: discord.Message):
    if message.content.lower().contains("happy halloween"):
        embed = Embed(title="Happy Halloween", description=message.author.mention, color=0x222222)
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/10/26/20/00/pumpkin-2892303_960_720.jpg")
        await message.channel.send(embed=embed)

client.run(tokens.TOKEN)