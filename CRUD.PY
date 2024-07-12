def crear_city(datos: dict):
    ciudades={}
    clear_screen()
    ciudades["nombre"]=input("Ingrese el nombre de la ciudad: ").lower()
    ciudades["codigo postal"]=input("Ingrese el codigo postal: ").lower()
    ciudades["poblacion"]=input("Ingrese poblacion de la ciudad: ").lower()
    ciudades["pais"]=input("Ingrese la duracion: ")
    
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
        # else: clear_screen()
        
# crear_cancion()

#ELIMINAR
def eliminar_song(datos: dict):
    clear_screen()
    nombre =input("Ingrese el nombre de la cancion: ").lower()
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == nombre:
            song = ("La cancion ",datos["ciudades"][i]["nombre"]," de ",datos["ciudades"][i]["artista"])
            datos["ciudades"].pop(i)
            separador = " "
            song = separador.join(map(str, song))
            print(song," ha sido eliminada con exito...")
            return datos
    print (f"La cancion ",nombre," no existe...")    
    return datos

def eliminar_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = eliminar_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        # else: clear_screen()
        
# eliminar_cancion()


#LEER
def leer_song(datos: dict):
    clear_screen()
    nombre =input("Ingrese el nombre de la cancion: ").lower()    
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
            print_("A r t i s t a")
            print_(datos["ciudades"][i]["artista"].capitalize())
            line()
            es()
            line()
            print_("G e n e r o")
            print_(datos["ciudades"][i]["genero"])
            line()
            es()
            line()
            print_("D u r a c i o n")
            print_(datos["ciudades"][i]["duracion"])
            line()
            es()
            line()
            print_("L a n z a m i e n t o")
            print_(datos["ciudades"][i]["lanzamiento"])
            line()
            es()
            line()
            print_("A l b u m")
            print_(datos["ciudades"][i]["album"].capitalize())
            line()
            es()
            linea()
            return datos
    print_(f"La cancion ",nombre," no existe...")    
    return datos

def leer_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = leer_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        # else: clear_screen()
        
# leer_cancion()


#ACTUALIZAR
def actualizar_song(datos: dict):
    clear_screen()
    nombre =input("Ingrese el nombre de la cancion: ").lower()    
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == nombre:
            while True:
                op = input("Ingrese una opcion:\n    0. Salir \n    1. Nombre\n    2. Artista\n    3. Genero\n    4. Duracion\n    5. Lanzamiento\n    6. Album\n\n>>  ")
                if op == "1": 
                    name =  datos["ciudades"][i]["nombre"]
                    datos["ciudades"][i]["nombre"]=input("Ingrese el nuevo nombre de la cancion: ").lower()
                    es()
                    print_(f"La cancion ",name," ha sido cambiada a ", datos["ciudades"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "2": 
                    name =  datos["ciudades"][i]["artista"]
                    datos["ciudades"][i]["artista"]=input("Ingrese el nuevo nombre del artista: ").lower()
                    es()
                    print_(f"El artista ",name," ha sido cambiada a ", datos["ciudades"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "3": 
                    name =  datos["ciudades"][i]["genero"]
                    while True:
                        op = input("Ingrese el nuevo genero de la cancion: \n    1. Rock\n    2. Pop\n    3. Urbana\n    4. Electronica\n    5. Rap\n>>    ")
                        if op == "1":
                            genero = datos["ciudades"][i]["genero"]
                            datos["ciudades"][i]["genero"] = "Rock"
                            datos["ciudades"][i]["genero_id"] = "01"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["ciudades"][i]["genero"]," con éxito!")
                            return datos
                        elif op == "2":
                            genero = datos["ciudades"][i]["genero"]
                            datos["ciudades"][i]["genero"] = "Pop"
                            datos["ciudades"][i]["genero_id"] = "02"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["ciudades"][i]["genero"]," con éxito!")
                            return datos
                        elif op == "3":
                            genero = datos["ciudades"][i]["genero"]
                            datos["ciudades"][i]["genero"] = "Urbana"
                            datos["ciudades"][i]["genero_id"] = "03"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["ciudades"][i]["genero"]," con éxito!")  
                            return datos
                        elif op == "4":
                            genero = datos["ciudades"][i]["genero"]
                            datos["ciudades"][i]["genero"] = "Electronica"
                            datos["ciudades"][i]["genero_id"] = "04"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["ciudades"][i]["genero"]," con éxito!")                  
                            return datos
                        elif op == "5":
                            genero = datos["ciudades"][i]["genero"]
                            datos["ciudades"][i]["genero"] = "Rap"
                            datos["ciudades"][i]["genero_id"] = "05" 
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["ciudades"][i]["genero"]," con éxito!")                  
                            return datos
                        else:
                            print_("El genero no es valido")
                elif op == "4": 
                    name =  datos["ciudades"][i]["nombre"]
                    dura =  datos["ciudades"][i]["duracion"]
                    datos["ciudades"][i]["duracion"]=input(f"Ingrese la nueva duracion: ").lower()
                    es()
                    print_(f"La duracion ",dura," ha sido cambiada a ", datos["ciudades"][i]["duracion"]," con éxito!")
                    return datos
                elif op == "5": 
                    name =  datos["ciudades"][i]["nombre"]
                    lanzamiento =  datos["ciudades"][i]["lanzamiento"]
                    datos["ciudades"][i]["lanzamiento"]=input(f"Ingrese el nuevo lanzamiento: ").lower()
                    es()
                    print_(f"El lanzamiento ",lanzamiento," ha sido cambiado a ", datos["ciudades"][i]["lanzamiento"]," con éxito!")
                    return datos
                elif op == "6":
                    name =  datos["ciudades"][i]["nombre"]
                    album =  datos["ciudades"][i]["album"]
                    datos["ciudades"][i]["album"]=input(f"Ingrese el nuevo album: ").lower()
                    es()
                    print_(f"El album ",album," ha sido cambiada a", datos["ciudades"][i]["album"],"con éxito!")
                    return datos
                elif op == "0": return datos 
                else: print_("Opcion no valida")
    print(f"La cancion",nombre,"no existe...")     
    return datos

def actualizar_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        datos = actualizar_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS)
        continuar = very()
        if continuar == "2": break
        # else: clear_screen()
        
# actualizar_cancion()
