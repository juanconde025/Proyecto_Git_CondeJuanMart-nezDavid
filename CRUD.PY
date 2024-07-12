def crear_ciudades(datos: dict):
    canciones={}
    clear_screen()
    diseño_logo_artista()
    canciones["nombre"]=input("Ingrese el nombre de la cancion: ").lower()
    canciones["artista"]=input("Ingrese el nombre del artista: ").lower()
    while True:
        op = input("Ingrese el genero de la cancion: \n    1. Rock\n    2. Pop\n    3. Urbana\n    4. Electronica\n    5. Rap\n>>    ")
        if op == "1": 
            canciones["genero"] = "Rock"
            canciones["genero_id"] = "01"             
            break
        elif op == "2":
            canciones["genero"] = "Pop"
            canciones["genero_id"] = "02"  
            break
        elif op == "3":
            canciones["genero"] = "Urbana"
            canciones["genero_id"] = "03"  
            break
        elif op == "4":
            canciones["genero"] = "Electronica"
            canciones["genero_id"] = "04"                   
            break
        elif op == "5":
            canciones["genero"] = "Rap"
            canciones["genero_id"] = "05"                   
            break
        else:
            print_("El genero no es valido")
    canciones["duracion"]=input("Ingrese la duracion: ")
    canciones["lanzamiento"]=input("Ingrese el lanzamiento de la cancion: ")
    canciones["album"]=input("Ingrese el nombre del album: ").lower()
    canciones["artista_id"]= contador_id()
    
    datos["canciones"].append(canciones)
    print(canciones["nombre"]," registrado con éxito!")
    return datos

def crear_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = crear_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# crear_cancion()

#ELIMINAR
def eliminar_song(datos: dict):
    clear_screen()
    diseño_logo_artista()
    nombre =input("Ingrese el nombre de la cancion: ").lower()
    for i in range(len(datos["canciones"])):
        if datos["canciones"][i]["nombre"] == nombre:
            song = ("La cancion ",datos["canciones"][i]["nombre"]," de ",datos["canciones"][i]["artista"])
            datos["canciones"].pop(i)
            separador = " "
            song = separador.join(map(str, song))
            print(song," ha sido eliminada con exito...")
            return datos
    print (f"La cancion ",nombre," no existe...")    
    return datos

def eliminar_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = eliminar_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# eliminar_cancion()


#LEER
def leer_song(datos: dict):
    clear_screen()
    diseño_logo_artista()
    nombre =input("Ingrese el nombre de la cancion: ").lower()    
    for i in range(len(datos["canciones"])):
        if datos["canciones"][i]["nombre"] == nombre:
            linea()
            es()
            line()
            print_("N o m b r e")
            print_(datos["canciones"][i]["nombre"].capitalize())
            line()
            es()
            line()
            print_("A r t i s t a")
            print_(datos["canciones"][i]["artista"].capitalize())
            line()
            es()
            line()
            print_("G e n e r o")
            print_(datos["canciones"][i]["genero"])
            line()
            es()
            line()
            print_("D u r a c i o n")
            print_(datos["canciones"][i]["duracion"])
            line()
            es()
            line()
            print_("L a n z a m i e n t o")
            print_(datos["canciones"][i]["lanzamiento"])
            line()
            es()
            line()
            print_("A l b u m")
            print_(datos["canciones"][i]["album"].capitalize())
            line()
            es()
            linea()
            return datos
    print_(f"La cancion ",nombre," no existe...")    
    return datos

def leer_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = leer_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# leer_cancion()


#ACTUALIZAR
def actualizar_song(datos: dict):
    clear_screen()
    diseño_logo_artista()
    nombre =input("Ingrese el nombre de la cancion: ").lower()    
    for i in range(len(datos["canciones"])):
        if datos["canciones"][i]["nombre"] == nombre:
            while True:
                op = input("Ingrese una opcion:\n    0. Salir \n    1. Nombre\n    2. Artista\n    3. Genero\n    4. Duracion\n    5. Lanzamiento\n    6. Album\n\n>>  ")
                if op == "1": 
                    name =  datos["canciones"][i]["nombre"]
                    datos["canciones"][i]["nombre"]=input("Ingrese el nuevo nombre de la cancion: ").lower()
                    es()
                    print_(f"La cancion ",name," ha sido cambiada a ", datos["canciones"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "2": 
                    name =  datos["canciones"][i]["artista"]
                    datos["canciones"][i]["artista"]=input("Ingrese el nuevo nombre del artista: ").lower()
                    es()
                    print_(f"El artista ",name," ha sido cambiada a ", datos["canciones"][i]["nombre"]," con éxito!")
                    return datos
                elif op == "3": 
                    name =  datos["canciones"][i]["genero"]
                    while True:
                        op = input("Ingrese el nuevo genero de la cancion: \n    1. Rock\n    2. Pop\n    3. Urbana\n    4. Electronica\n    5. Rap\n>>    ")
                        if op == "1":
                            genero = datos["canciones"][i]["genero"]
                            datos["canciones"][i]["genero"] = "Rock"
                            datos["canciones"][i]["genero_id"] = "01"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["canciones"][i]["genero"]," con éxito!")
                            return datos
                        elif op == "2":
                            genero = datos["canciones"][i]["genero"]
                            datos["canciones"][i]["genero"] = "Pop"
                            datos["canciones"][i]["genero_id"] = "02"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["canciones"][i]["genero"]," con éxito!")
                            return datos
                        elif op == "3":
                            genero = datos["canciones"][i]["genero"]
                            datos["canciones"][i]["genero"] = "Urbana"
                            datos["canciones"][i]["genero_id"] = "03"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["canciones"][i]["genero"]," con éxito!")  
                            return datos
                        elif op == "4":
                            genero = datos["canciones"][i]["genero"]
                            datos["canciones"][i]["genero"] = "Electronica"
                            datos["canciones"][i]["genero_id"] = "04"
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["canciones"][i]["genero"]," con éxito!")                  
                            return datos
                        elif op == "5":
                            genero = datos["canciones"][i]["genero"]
                            datos["canciones"][i]["genero"] = "Rap"
                            datos["canciones"][i]["genero_id"] = "05" 
                            es()
                            print_(f"El genero ",genero," ha sido cambiada a ", datos["canciones"][i]["genero"]," con éxito!")                  
                            return datos
                        else:
                            print_("El genero no es valido")
                elif op == "4": 
                    name =  datos["canciones"][i]["nombre"]
                    dura =  datos["canciones"][i]["duracion"]
                    datos["canciones"][i]["duracion"]=input(f"Ingrese la nueva duracion: ").lower()
                    es()
                    print_(f"La duracion ",dura," ha sido cambiada a ", datos["canciones"][i]["duracion"]," con éxito!")
                    return datos
                elif op == "5": 
                    name =  datos["canciones"][i]["nombre"]
                    lanzamiento =  datos["canciones"][i]["lanzamiento"]
                    datos["canciones"][i]["lanzamiento"]=input(f"Ingrese el nuevo lanzamiento: ").lower()
                    es()
                    print_(f"El lanzamiento ",lanzamiento," ha sido cambiado a ", datos["canciones"][i]["lanzamiento"]," con éxito!")
                    return datos
                elif op == "6":
                    name =  datos["canciones"][i]["nombre"]
                    album =  datos["canciones"][i]["album"]
                    datos["canciones"][i]["album"]=input(f"Ingrese el nuevo album: ").lower()
                    es()
                    print_(f"El album ",album," ha sido cambiada a", datos["canciones"][i]["album"],"con éxito!")
                    return datos
                elif op == "0": return datos 
                else: print_("Opcion no valida")
    print(f"La cancion",nombre,"no existe...")     
    return datos

def actualizar_cancion():
    while True:
        datos = cargar_datos(RUTA_BASE_DE_DATOS_ARTISTAS)
        datos = actualizar_song(datos)
        guardar_datos(datos, RUTA_BASE_DE_DATOS_ARTISTAS)
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
        
# actualizar_cancion()
