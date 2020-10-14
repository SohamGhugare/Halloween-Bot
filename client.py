import asyncio
import discord
from discord.embeds import Embed
import tokens
from discord import Client, Activity, ActivityType

client = Client()

@client.event
async def on_ready():
    print("Client is ready")
    activity = Activity(name="Halloween 🎃👻 | -help", type=ActivityType.streaming)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message: discord.Message):
    if "happy halloween" in message.content.lower():
        await message.channel.trigger_typing()
        embed = Embed(title="Happy Halloween", description=message.author.mention, color=0x222222)
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2017/10/26/20/00/pumpkin-2892303_960_720.jpg")
        await message.channel.send(embed=embed)
    if "kill me" in message.content.lower():
        with message.channel.typing():
            await asyncio.sleep(7)
            embed = Embed(title="Muhahaha!\nhere i am to kill you", description=f"{message.author.mention} you wanted someone to kill you na!", color=0xff2222)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/748941782427107449/765916527718694912/ghost_reaper.jpg")
            await message.channel.send(embed=embed)

client.run(tokens.TOKEN)