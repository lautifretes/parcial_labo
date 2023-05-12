import re

def parse_habilidades(habilidades:str):
        habilidades = habilidades.split("|$%")
        habilidades[-1] = habilidades[-1].replace("\n","")
        for habilidad in habilidades:
            habilidad = habilidad.rstrip()
        return habilidades

def parse_raza(raza:str):
    raza = raza.split("-")
    return raza



def parse_csv(ruta:str)->list:
    lista_personajes = []
    archivo = open(ruta, "r",encoding = "utf-8")
    for linea in archivo:
        lectura = re.split(",", linea)
        personajes = {}
        personajes["id"] = lectura[0]
        personajes["Nombre"] = lectura[1]
        personajes["Raza"] = parse_raza(lectura[2])
        personajes["Poder de pelea"] = int(lectura[3])
        personajes["Poder de ataque"] = int(lectura[4])
        personajes["Habilidades"] = parse_habilidades(lectura[5])
        lista_personajes.append(personajes)

    return lista_personajes


lista_dbz = parse_csv("DBZ.csv")
print(lista_dbz)




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