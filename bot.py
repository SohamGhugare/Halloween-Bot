from os import name
import discord
from discord.ext import commands
import datetime
import asyncio
import subprocess as sb
from dotenv import load_dotenv
import tokens
from threading import Thread

load_dotenv()

emoji = ['🎃', '👻', '🌟', '✨']

# Bot invite link :
# https://discord.com/api/oauth2/authorize?client_id=763634248115945483&permissions=2080898160&scope=bot

def client_thread():
    sb.run("python client.py")

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
    async with ctx.typing():
        await ctx.send(f'{ctx.author.mention} You are being possessed..... {emoji[1]}')
        await asyncio.sleep(2)
        await ctx.send(f'Converting to ghost..... {emoji[1]}')
        await asyncio.sleep(2)
        await ctx.send(f'You are now possessed, Welcome to the Spooked family!')
        await ctx.send(emoji[1])
        user: discord.Member = ctx.author
        await user.edit(nick=(user.nick or user.name) + emoji[1])


# ------ EVENT COMMAND ----------

@bot.command(aliases=['Event'])
@commands.has_role('Event Host')
async def event(ctx, cmd):
    if cmd.lower() == "host":
        embed = discord.Embed(title='EVENT !!', color=discord.Color.green())
        embed.add_field(name=f'A new event has been hosted by {ctx.author.name} !', value = 'React to this message within 10 secs to enter in the event !')
        msg: discord.Message = await ctx.send(embed = embed)
        await msg.add_reaction('🎉')
        await asyncio.sleep(10) #Change as per required
        new_msg: discord.Message = await ctx.channel.fetch_message(msg.id)

        members = await new_msg.reactions[0].users().flatten()
        members.pop(members.index(bot.user))
        await new_msg.delete()
        membed = discord.Embed(title='Members Enrolled: ', description="\n".join(x.mention for x in members), color=discord.Color.red())
        await ctx.send(embed = membed)
        mem: discord.User
        for mem in members:
            chan: discord.DMChannel = mem.dm_channel or await mem.create_dm()
            await chan.trigger_typing()
            await chan.send("testing eh?")


 


# Help command

bot.remove_command('help')

@bot.command(aliases=['Help'])
async def help(ctx):
    await ctx.trigger_typing()
    embed = discord.Embed(title='Commands:', color=discord.Color.green())

    embed.add_field(name='-halloween', value='Shows days remaining for Halloween')
    embed.add_field(name='-possess', value='Converts you into Spooked Family')
    embed.add_field(name='-event host', value='Hosts an event (Needs "Event Host" role')

    embed.set_footer(icon_url = ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)

client = Thread(target=client_thread)
client.start()

bot.run(tokens.TOKEN)