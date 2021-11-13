from listar import agenda
from colorama import init, Fore

def buscar_contacto(nombre):
    if nombre in agenda.keys():
        print(Fore.GREEN +'Nombre:'+Fore.WHITE+ nombre, agenda[nombre])
    else:
        print('El nombre no se encuentra en el directorio')
