# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=',')

@bot.command(
    name='saludo', 
    help='Manda un saludo por el chat',
    aliases=['hola','hi','hello']
    )
async def greetings(ctx):
    await ctx.send('Saludos, soy sten-bot, que las runas te sean propicias.')

@bot.command(
    name='runas', 
    help='Lanza X runas.',
    aliases=['r']
    )
async def roll(ctx, number_of_runes: int):
    result = 0
    i = 0
    while i < number_of_runes:
        result += random.randint(0,1)
        i += 1
    
    await ctx.send(f'{ctx.author} tira {number_of_runes} runas obteniendo {result} éxitos.')

bot.run(TOKEN)
