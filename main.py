from funciones import *
from os import system
system("cls")


seguir = True
while seguir == True:
    
    mostar_menu()

    respuesta = int(input("Ingrese un numero: "))
    match respuesta:
        case 1:
            print(lista_dbz)
        case 2:
            pass
        case 3:
            listar_por_clave(lista_dbz, "Raza")
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            seguir == False
