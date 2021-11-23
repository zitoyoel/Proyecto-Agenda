from listar import agenda;
from conversiones import diccionario_a_archivo
from colorama import init, Fore, Back
init(autoreset=True)

def eliminar_contacto(nombre):
    if nombre in agenda.keys():
        del agenda[nombre]
        diccionario_a_archivo()
        print(Fore.WHITE + Back.GREEN +'Contacto eliminado')
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')
