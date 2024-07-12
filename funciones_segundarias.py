import os
import platform
from datetime import datetime
import shutil

def clear_screen():
    if platform.system() == 'Windows': os.system('cls')
    else: os.system('clear')

def very():
    while True:
        linen()
        print_("¿Repetir operacion?")
        print_("1 .Si")
        print_("2 .No")
        continuar = input("                     >>>")
        linen()
        if continuar == "1": return "1"
        elif continuar == "2": 
            clear_screen()
            return "2"
        else: print_ ("Opcion no valida")

def print_(*args, **kwargs):
    ancho_consola = shutil.get_terminal_size().columns
    texto = ' '.join(map(str, args))
    ancho_espacios = kwargs.get('ancho_espacios', 1)
    espacio_blancos = (ancho_consola - len(texto)) // 2
    print(' ' * espacio_blancos + texto.center(ancho_consola - 2 * espacio_blancos))

def line():
    ancho_consola = shutil.get_terminal_size().columns
    return print("-" * ancho_consola)

def linen():
    ancho_consola = shutil.get_terminal_size().columns
    return print("." * ancho_consola)

def linea():
    ancho_consola = shutil.get_terminal_size().columns
    return print("_" * ancho_consola)
def es():
    print(" ")

def diseño_logo():
    linen()
    print('''\033[1;33m

  /$$$$$$  /$$$$$$ /$$$$$$$$ /$$     /$$ /$$   /$$  /$$$$$$  /$$    /$$
 /$$__  $$|_  $$_/|__  $$__/|  $$   /$$/| $$$ | $$ /$$__  $$| $$   | $$
| $$  \__/  | $$     | $$    \  $$ /$$/ | $$$$| $$| $$  \ $$| $$   | $$
| $$        | $$     | $$     \  $$$$/  | $$ $$ $$| $$$$$$$$|  $$ / $$/
| $$        | $$     | $$      \  $$/   | $$  $$$$| $$__  $$ \  $$ $$/ 
| $$    $$  | $$     | $$       | $$    | $$\  $$$| $$  | $$  \  $$$/  
|  $$$$$$/ /$$$$$$   | $$       | $$    | $$ \  $$| $$  | $$   \  $/   
 \______/ |______/   |__/       |__/    |__/  \__/|__/  |__/    \_/    
  
  \033[0m''')
    linen()