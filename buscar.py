from listar import agenda
from colorama import init, Fore, Back

def buscar_contacto(nombre):
    if nombre in agenda.keys():
        print(Fore.GREEN +'Nombre:'+Fore.WHITE+ nombre, agenda[nombre])
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')
