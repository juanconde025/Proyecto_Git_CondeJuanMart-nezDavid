from menu import *
from datos import *
from CRUD import *
from funciones_segundarias import *

while True:
    clear_screen()
    diseño_logo()
    menu_principal()
    opcion = input(">> ")
    if opcion == "1": crear_ciudad()
    elif opcion == "2": actualizar_ciudad()
    elif opcion == "3": leer_ciudad()
    elif opcion == "4": leer_ciudades()
    elif opcion == "5": break
    else: print("Opcion no valida")