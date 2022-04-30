import textwrap

# Sheet width and height in character
width = 79
height = 13

character = {
    "nombre": "Lia Raudyir",
    "nivel": 4,
    "habilidades": {
        "detección": 1,
        "escalada": 3,
        "herbolaria": 3,
        "manejo de lanza": 2,
        "orientación": 3,
        "rastreo": 3,
        "sigilo": 2,
        "supervivencia": 3
    },
    "mano derecha": "lanza ligera",
    "mano izquierda": "nada",
    "torso": "protección ligera de cuero",
    "cualidades especiales": {
        "combate conjunto",
        "agresivo",
        "animal"
        }
}

def init_sheet():
    sheet = [[' ']*height for i in range(width)]
    return sheet

def print_sheet(sheet):
    j = 0
    while j < height:
        line = ''

        i = 0
        while i < width:
            line += sheet[i][j]
            i += 1

        j += 1

        print(line)

def draw_border(sheet):
    for x in range(width):
        sheet[x][0] = '\u2500'

    for x in range(width):
        sheet[x][height-1] = '\u2500'

    for y in range(height):
        sheet[0][y] = '\u2502'

    for y in range(height):
        sheet[width-1][y] = '\u2502'

    for y in range(height):
        sheet[round(width/2)][y] = '\u2502'

    sheet[0][0] = '\u250c'
    sheet[width-1][0] = '\u2510'
    sheet[0][height-1] = '\u2514'
    sheet[width-1][height-1] = '\u2518'

    sheet[round(width/2)][0] = '\u252c'
    sheet[round(width/2)][height-1] = '\u2534'

    return sheet


def write_text(text, x, y, sheet):
    i = 0
    j = 0

    for char in text:
        if char == '\n':
            j += 1
            i = 0
        else:
            sheet[x+i][y+j] = char
            i += 1

    return sheet

def get_habilidades(character):

    habilidades = 'Habilidades:'
    
    for habilidad in character["habilidades"]:
        nivel = character["habilidades"][habilidad]
        habilidades += f' {habilidad} {nivel},'

    habilidades = habilidades[:-1]
    habilidades += '.'
    habilidades = habilidades[::-1].replace(',','y ',1)[::-1]

    return habilidades

def get_equipo(character):
    equipo = 'Equipo:'

    if character['mano derecha'] != 'nada':
        equipo += f' {character["mano derecha"]},'

    if character['mano izquierda'] != 'nada':
        equipo += f' {character["mano izquierda"]},'

    if character['torso'] != 'nada':
        equipo += f' {character["torso"]},'

    equipo = equipo[:-1]
    equipo += '.'
    equipo = equipo[::-1].replace(',','y ',1)[::-1]

    return equipo

def get_cualidades_especiales(character):
    text = 'Cualidades especiales:'

    for cualidad_especial in character['cualidades especiales']:
        text+= f' {cualidad_especial},'

    text = text[:-1]
    text += '.'
    text = text[::-1].replace(',','y ',1)[::-1]

    return text

sheet = init_sheet()

sheet = draw_border(sheet)

sheet = write_text(' Reglas especiales y equipo ', 2, 0, sheet)

sheet = write_text(f' {character["nombre"]} ', round(width/2)+2, 0, sheet)

sheet = write_text(f'[{character["nivel"]}]', width-5, 0, sheet)

#text =  '''Atributos  Cualidades
#F2 V2 P2   Agu 15 Ini 9 Vid 10
#A3 I3 D1   Luz  1 Osc 1 Ele  2
#R3 L1 E1   SN   3
#
#Combate
#Imp Dañ  TiD          Est Alc Peso
#  4   5  per            3   3  1.5
#Eva Cob  Con Cor Per  Est Pen Peso
#  3   4    0   2   2    1   0    5
#'''
text =  '''
F2  Vid 10  Im     4   4
A3  Ini  9  Da     5   5
R3  Agu 15  TiD  per per
            Est    3   3
V2  Con  0  Alc    3   3
I3  Cor  2  
L1  Per  2  
    Luz  1  Eva   3
P2  Osc  1  Cob   4
D1  Ele  2  Est   1
E1  SN   3  Pen   0
'''
sheet = write_text(text, round(width/2)+2, 0, sheet)

text = '\n'.join(textwrap.wrap(get_equipo(character),width=37,subsequent_indent=' '))
text += '\n'
text += '\n'.join(textwrap.wrap(get_habilidades(character),width=37,subsequent_indent=' '))
text += '\n'
text += '\n'.join(textwrap.wrap(get_cualidades_especiales(character),width=37,subsequent_indent=' '))

sheet = write_text(text, 2, 1, sheet)

print_sheet(sheet)

