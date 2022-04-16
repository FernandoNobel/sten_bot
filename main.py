# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from tabulate import tabulate

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=',')

bot.combat_data = []

#bot.combat_data.append({
#    'id': 1,
#    'name': 'Lobo',
#    'ini': 5,
#    'agu': 6,
#    'vid': 7,
#    'est': 8
#    })
#
#bot.combat_data.append({
#    'id': 2,
#    'name': 'Guerrero',
#    'ini': 10,
#    'agu': 6,
#    'vid': 7,
#    'est': 8
#    })
#
#bot.combat_data.append({
#    'id': 3,
#    'name': 'Soldado',
#    'ini': 8,
#    'agu': 6,
#    'vid': 7,
#    'est': 8
#    })

def print_combat_table():
    # In this variable we prepare the data to show in the combat table.
    data = [] 

    # Prepare the data of each character and add it to data.
    for character in bot.combat_data:
        pj = []

        pj.append( character['id'] )
        pj.append( character['nombre'] )
        pj.append( character['ini'] )
        pj.append( character['agu'] )
        pj.append( character['vid'] )
        pj.append( character['est'] )

        data.append(pj)

    # Sort the characters by initiative.
    data = sorted(data, key=lambda x: x[2], reverse=True)

    # Prepare the combat_table text to send to discord.
    result = '**Mesa de combate**\n'
    result += '```\n' 
    result += (tabulate(data, headers=["Id", "Nombre", "Ini", "Agu", "Vid", "Est"])) 
    result += '\n```'

    return result
 
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


@bot.command(
    name='mesa_de_combate', 
    help='Muestra la mesa de combate.',
    aliases=['c']
    )
async def combat_table(ctx):
    await ctx.send(print_combat_table())

@bot.command(
    name='new', 
    help='Añade un nuevo personaje a la mesa de combate.'
    )
async def new_character(ctx):
    highest_id = 0

    for character in bot.combat_data:
        if character['id'] > highest_id:
            highest_id = character['id']

    character =  {
        'id': highest_id+1,
        'nombre': 'sin-nombre',
        'ini': 0,
        'agu': 0,
        'vid': 0,
        'est': 0
        }

    bot.combat_data.append(character)
    
    await ctx.send(print_combat_table())

@bot.command(
    name='clean', 
    help='Limpia la mesa de combate'
    )
async def clean(ctx):
    bot.combat_data = []
    await ctx.send(print_combat_table())

@bot.command(
    name='modify', 
    help='Modifica un parametro de un personaje'
    )
async def modify_character(ctx, id: int, parameter_name: str, parameter_value):

    i = 0

    parameter_name = parameter_name.lower()

    if parameter_name == 'id':
        return

    if parameter_name == 'nombre':
        parameter_value = str(parameter_value)
    else:
        parameter_value = int(parameter_value)

    while i < len(bot.combat_data):
        if (bot.combat_data[i])['id'] == id:
            (bot.combat_data[i])[parameter_name] = parameter_value
            break
        i += 1

    await ctx.send(print_combat_table())

bot.run(TOKEN)
