#Fretes Lautaro
#1B

from os import system
system("cls")

import re

def parse_habilidades(habilidades:str):
        habilidades = habilidades.split("|$%")
        habilidades[-1] = habilidades[-1].replace("\n","")
        for habilidad in habilidades:
            habilidad = re.sub("\\s", "",habilidad)
        return habilidades

def parse_raza(raza:str):
    raza = raza.split("-")
    return raza

print(type(parse_raza("alumno-lo")))

def parser_csv(path:str)->list:
    lista_persojanes = []
    with open(path, encoding="utf-8") as archivo:
        for line in archivo:
            indice = re.split("[,\n]", line)
            #indice = re.sub("[]","", line)

            personajes = {}
            personajes["Id"] = indice[0]
            personajes["Nombre"] = indice[1]
            personajes["Raza"] = parse_raza(indice[2])  
            personajes["Poder de pelea"] = int(indice[3])
            #indice[3] = int(indice[3])
            personajes["Poder de defensa"] = int(indice[4])
            # indice[4] = int(indice[4])
            personajes["Habilidades"] = parse_habilidades(indice[5])
            
            lista_persojanes.append(personajes)

    return lista_persojanes 

ruta = "DBZ.csv"
lista_dbz = parser_csv(ruta)
print(lista_dbz)






print("########################################################################")

menu = ["###################\n1. Traer datos de archivo csv\n2. Listar cantidad por raza\n3. Listar personajes por raza\n4. Listar personajes por habilidad\n5. Jugar batalla\n6. Guardar en Json\n7. Leer Json\n8. Salir "]

def mostar_menu():
    #muestro menu
    for opcion in menu:
        print(opcion)




def listar_por_clave(lista:list, clave:str, clave_dos = None):
    lista_raza=[]
    for personaje in lista:
        raza = personaje[clave]
        lista_raza.append(raza)
    lista_raza_filtrada = set(lista_raza)

    for raza in lista_raza_filtrada:
        print(raza)
        for personaje in lista:
            if personaje[clave] == raza:
                print(f"\t{personaje['Nombre']} - Poder de pelea: {personaje['Poder de pelea']}")




listar_por_clave(lista_dbz,"Raza")
print("########################################################################")
##################################")

def contar_por_clave(lista:list, clave:str):
    lista_raza=[]
    for personaje in lista:
        raza = personaje[clave]
        lista_raza.append(raza)
    lista_raza_filtrada = set(lista_raza)
    lista_raza_filtrada = list(lista_raza_filtrada)

    for raza in lista_raza_filtrada:
        contador = 0
        print(f"los personajes que tiene la razaa {raza} es: ")
        for personaje in lista:
            if personaje[clave] == raza:
                contador += 1
        return contador
    
contadooiiiir = contar_por_clave(lista_dbz,"Raza")
print(contadooiiiir)

print("########################################################################")


