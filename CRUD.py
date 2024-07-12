from datos import *
from funciones_segundarias import *

def crear_city(datos: dict):
    ciudades={}
    clear_screen()
    ciudades["nombre"]=input("Ingrese el nombre de la ciudad: ").lower()
    ciudades["codigo postal"]=input("Ingrese el codigo postal: ").lower()
    ciudades["poblacion"]=input("Ingrese poblacion de la ciudad: ").lower()
    ciudades["pais"]=input("Ingrese el pais: ")
    
    datos["ciudades"].append(ciudades)
    print(ciudades["nombre"]," ha sido registrada con éxito!")
    return datos

def crear_ciudad():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = crear_city(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()


#LEER
def leer_city(datos: dict):
    clear_screen()
    nombre =input("Ingrese el nombre de la ciudad: ").lower()    
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == nombre:
            linea()
            es()
            line()
            print_("N o m b r e")
            print_(datos["ciudades"][i]["nombre"].capitalize())
            line()
            es()
            line()
            print_("C o d i g o  P o s t a l")
            print_(datos["ciudades"][i]["codigo postal"].capitalize())
            line()
            es()
            line()
            print_("P o b l a c i o n")
            print_(datos["ciudades"][i]["poblacion"])
            line()
            es()
            line()
            print_("P a i s")
            print_(datos["ciudades"][i]["pais"].capitalize())
            line()
            es()
            linea()
            return datos
    print_(f"La ciudad ",nombre," no existe...")    
    return datos

def leer_ciudad():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = leer_city(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

def leer_citys(datos: dict):
    clear_screen()
    print_("C i u d a d e s")
    for sn in range(len(datos["ciudades"])):
        print_(datos["ciudades"][sn]["nombre"].capitalize())
    for i in range(len(datos["ciudades"])):
        linea()
        es()
        line()
        print_("N o m b r e")
        print_(datos["ciudades"][i]["nombre"].capitalize())
        line()
        es()
        line()
        print_("C o d i g o  P o s t a l")
        print_(datos["ciudades"][i]["codigo postal"].capitalize())
        line()
        es()
        line()
        print_("P o b l a c i o n")
        print_(datos["ciudades"][i]["poblacion"])
        line()
        es()
        line()
        print_("P a i s")
        print_(datos["ciudades"][i]["pais"].capitalize())
        line()
        es()
        linea()
    return datos
def leer_ciudades():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = leer_citys(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

#ACTUALIZAR
def actualizar_city(datos: dict):
    clear_screen()
    nombre =input("Ingrese el nombre de la ciudad: ").lower()    
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == nombre:
            while True:
                op = input("Ingrese una opcion:\n    0. Salir \n    1. Nombre\n    2. codigo postal\n    3. Poblacion\n    4. Pais\n\n>>  ")
                if op == "1": 
                    name =  datos["ciudades"][i]["nombre"]
                    datos["ciudades"][i]["nombre"]=input("Ingrese el nuevo nombre de la ciudad: ").lower()
                    es()
                    print_(f"La ciudad ",name," ha sido cambiada a ", datos["ciudades"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "2": 
                    name =  datos["ciudades"][i]["codigo postal"]
                    datos["ciudades"][i]["codigo postal"]=input("Ingrese el nuevo codigo postal de la ciudad: ").lower()
                    es()
                    print_(f"La ciudad ",name," ha sido cambiada a ", datos["ciudades"][i]["codigo postal"]," con éxito!")
                    return datos
                elif op == "3": 
                    name =  datos["ciudades"][i]["poblacion"]
                    datos["ciudades"][i]["poblacion"]=input("Ingrese la nueva poblacion de la ciudad: ")
                    es()
                    print_(f"La poblacion ",name," ha sido cambiada a ", datos["ciudades"][i]["poblacion"]," con éxito!")
                    return datos
                elif op == "4": 
                    name =  datos["ciudades"][i]["pais"]
                    datos["ciudades"][i]["pais"]=input("Ingrese el nuevo pais de la ciudad: ")
                    es()
                    print_(f"El pais ",name," ha sido cambiada a ", datos["ciudades"][i]["pais"]," con éxito!")
                    return datos
               
                elif op == "0": return datos 
                else: print_("Opcion no valida")
    print(f"La ciudad",nombre,"no existe...")     
    return datos

def actualizar_ciudad():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = actualizar_city(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
