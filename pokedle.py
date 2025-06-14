import csv
from collections import namedtuple
import random
from datetime import date

day = str(date.today())
pokeday = int(day.replace('-', ''))
random.seed(pokeday)

poketuple = namedtuple("poketuple", ['type1', 'type2', 'gen', 'evo', 'height', 'weight', 'dex'])

with open('full pokedle csv.csv', newline='') as pokecsv:
  pokereader = csv.reader(pokecsv, delimiter=',')
  next(pokereader)
  pokedict = {pokeline[1]: poketuple(pokeline[2], pokeline[3], int(pokeline[5]), pokeline[4], float(pokeline[6]), float(pokeline[7]), int(pokeline[0])) for pokeline in pokereader}

pokelist = [pokemon for pokemon in pokedict]
pokeseed = random.randint(0, len(pokelist) - 1)
pokedle = pokelist[pokeseed]
pokedleT = pokedict[pokedle]
print(r"""
 ______    _____   _    _  _______  _____    _        _______ 
(_____ \  / ___ \ | |  / )(_______)(____ \  | |      (_______)
 _____) )| |   | || | / /  _____    _   \ \ | |       _____   
|  ____/ | |   | || |< <  |  ___)  | |   | || |      |  ___)  
| |      | |___| || | \ \ | |_____ | |__/ / | |_____ | |_____ 
|_|       \_____/ |_|  \_)|_______)|_____/  |_______)|_______)
""")
print(r"""
                                      _                                                                             _                _ 
                                     | |                                                                           | |              | |
 ____    ____  _ _ _    ____    ___  | |  _   ____  ____    ___   ____      ____  _   _   ____   ____  _   _     _ | |  ____  _   _ | |
|  _ \  / _  )| | | |  |  _ \  / _ \ | | / ) / _  )|    \  / _ \ |  _ \    / _  )| | | | / _  ) / ___)| | | |   / || | / _  || | | ||_|
| | | |( (/ / | | | |  | | | || |_| || |< ( ( (/ / | | | || |_| || | | |  ( (/ /  \ V / ( (/ / | |    | |_| |  ( (_| |( ( | || |_| | _ 
|_| |_| \____) \____|  | ||_/  \___/ |_| \_) \____)|_|_|_| \___/ |_| |_|   \____)  \_/   \____)|_|     \__  |   \____| \_||_| \__  ||_|
                       |_|                                                                            (____/                 (____/
""")
pokechoice = input('Enter a Pokemon (capitalized and double check your spelling pls)\n')
while pokechoice not in pokedict:
  pokechoice = input('<LOUD INCORRECT BUZZER> das not in da list. try again \n')
print("Type 1 | Type 2 | Generation | Evo. Stage | Height | Weight | Pokedex No.")

while pokechoice != pokedle:
  pokechoiceT = pokedict[pokechoice]
# checking type 1
  if pokechoiceT.type1 == pokedleT.type2:
    type1 = '\033[43m'
  elif pokechoiceT.type1 == pokedleT.type1:
    type1 = '\033[42m'
  else:
    type1 = '\033[41m'
  type1 += pokechoiceT.type1.center(7)
# checking type 2
  if pokechoiceT.type2 == pokedleT.type1:
    type2 = '\033[43m'
  elif pokechoiceT.type2 == pokedleT.type2:
    type2 = '\033[42m'
  else:
    type2 = '\033[41m'
  type2 += pokechoiceT.type2.center(8)
# checking generation
  if pokechoiceT.gen == pokedleT.gen:
    gen = '\033[42m' + (str(pokechoiceT.gen) + '=').center(12)
  elif pokechoiceT.gen < pokedleT.gen:
    gen = '\033[41m' + (str(pokechoiceT.gen) + '^').center(12)
  else:
    gen = '\033[41m' + (str(pokechoiceT.gen) + 'v').center(12)
# checking evolution stage
  if pokechoiceT.evo == pokedleT.evo:
    if pokedleT.evo == 'Mega':
      evo = '\033[42m' + pokechoiceT.evo.center(12)
    evo = '\033[42m' + (pokechoiceT.evo + '=').center(12)
  elif pokechoiceT.evo < pokedleT.evo:
    evo = '\033[41m' + (pokechoiceT.evo + '^').center(12)
  else:
    evo = '\033[41m' + (pokechoiceT.evo + 'v').center(12)
# checking height
  pokeheight = f'{pokechoiceT.height:04.1f}'
  if pokechoiceT.height == pokedleT.height:
    height = '\033[42m' + ('=' + pokeheight + '=').center(8)
  elif pokechoiceT.height < pokedleT.height:
    height = '\033[41m' + ('^' + pokeheight + '^').center(8)
  else:
    height = '\033[41m' + ('v' + pokeheight + 'v').center(8)
# checking weight
  pokeweight = f'{pokechoiceT.weight:05.1f}'
  if pokechoiceT.weight == pokedleT.weight:
    weight = '\033[42m' + (pokeweight + '=').center(8)
  elif pokechoiceT.weight < pokedleT.weight:
    weight = '\033[41m' + (pokeweight + '^').center(8)
  else:
    weight = '\033[41m' + (pokeweight + 'v').center(8)
# checking pokedex number
  pokedex = f'{pokechoiceT.dex:03d}'
  if pokechoiceT.dex == pokedleT.dex:
    dex = '\033[42m' + (pokedex + '=').center(12)
  elif pokechoiceT.dex < pokedleT.dex:
    dex = '\033[41m' + (pokedex + '^').center(12)
  else:
    dex = '\033[41m' + (pokedex + 'v').center(12)
  print(type1 + '\033[0m|' + type2 + '\033[0m|' + gen + '\033[0m|' + evo + '\033[0m|' + height + '\033[0m|' + weight + '\033[0m|' + dex + '\033[0m')
  print('wrong answer forehead')
  pokechoice = input('Try again :)\n')
  while pokechoice not in pokedict:
    pokechoice = input('<LOUD INCORRECT BUZZER> das not in da list. try again \n')
print('NICE JOB GUY')