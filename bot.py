import discord
from discord.ext import commands
import datetime
import asyncio
import os
from dotenv import load_dotenv
import tokens
from threading import Thread

load_dotenv()

emoji = ['🎃', '👻', '🌟', '✨']

# Bot invite link :
# https://discord.com/api/oauth2/authorize?client_id=763634248115945483&permissions=2080898160&scope=bot

def client_thread():
    os.system("python client.py")

bot = commands.Bot(command_prefix = "-")

@bot.event
async def on_ready():
    print("Bot is online!")

# Halloween days remaining

today = datetime.date.today()
days = datetime.date(today.year, 10, 31)
remain = days - today

@bot.command(aliases=['Halloween', 'hl', 'Hl', 'HL'])
async def halloween(ctx):
    embed = discord.Embed(title=f'{emoji[0]} Halloween is in {remain.days} days !! {emoji[0]}')

    await ctx.send(embed = embed)


# Possess command

@bot.command(aliases=['Possess', 'p'])
async def possess(ctx):
    await ctx.send(f'{ctx.author.mention} You are being possessed..... {emoji[1]}')
    await asyncio.sleep(2)
    await ctx.send(f'Converting to ghost..... {emoji[1]}')
    await asyncio.sleep(2)
    await ctx.send(f'You are now possessed, Welcome to the Spooked family!{emoji[1]}')


# Help command

bot.remove_command('help')

@bot.command(aliases=['Help'])
async def help(ctx):
    embed = discord.Embed(title='Commands:', color=discord.Color.green())

    embed.add_field(name='-halloween', value='Shows days remaining for Halloween')
    embed.add_field(name='-possess', value='Converts you into Spooked Family')

    embed.set_footer(icon_url = ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)

client = Thread(target=client_thread, daemon=True)
client.run()

Thread(target=bot.run, args=(tokens.TOKEN,)).run()