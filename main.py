# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from tabulate import tabulate
import copy

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=',')

bot.combat_data = []

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

def generate_new_id():
    highest_id = 0

    for character in bot.combat_data:
        if character['id'] > highest_id:
            highest_id = character['id']

    new_id = highest_id + 1

    return new_id

def modify_character(character_id, parameter_name, parameter_value):

    parameter_name = parameter_name.lower()

    if parameter_name == 'id':
        return

    if parameter_name == 'nombre':
        parameter_value = str(parameter_value)
    else:
        parameter_value = int(parameter_value)

    i = 0
    while i < len(bot.combat_data):
        if (bot.combat_data[i])['id'] == character_id:
            (bot.combat_data[i])[parameter_name] = parameter_value
            break
        i += 1

    return

@bot.command(
    name='greetings', 
    help='Manda un saludo por el chat',
    aliases=['g']
    )
async def greetings(ctx):
    await ctx.send('Saludos, soy sten-bot, que las runas te sean propicias.')

@bot.command(
    name='roll', 
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
    name='show', 
    help='Muestra la mesa de combate.',
    aliases=['s']
    )
async def show(ctx):
    await ctx.send(print_combat_table())

@bot.command(
    name='new', 
    help='Añade un nuevo personaje a la mesa de combate.',
    aliases=['n']
    )
async def new(ctx, *args):
    character_id = generate_new_id()

    character =  {
        'id': character_id,
        'nombre': 'sin-nombre',
        'ini': 0,
        'agu': 0,
        'vid': 0,
        'est': 0
        }

    bot.combat_data.append(character)

    i = 0

    while i < len(args):
        modify_character(character_id, args[i], args[i+1])
        i += 2

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
    help='Modifica un parametro de un personaje',
    aliases=['m']
    )
async def modify(ctx, character_id: int, parameter_name: str, parameter_value):

    modify_character(character_id, parameter_name, parameter_value)

    await ctx.send(print_combat_table())

@bot.command(
    name='duplicate', 
    help='Crea una copia de un personaje',
    aliases=['d']
    )
async def duplicate(ctx, character_id: int):

    i = 0
    while i < len(bot.combat_data):
        if (bot.combat_data[i])['id'] == character_id:

            clone = copy.copy(bot.combat_data[i])
            clone['id'] = generate_new_id()
            bot.combat_data.append(clone)

            break
        i += 1

    await ctx.send(print_combat_table())

bot.run(TOKEN)
