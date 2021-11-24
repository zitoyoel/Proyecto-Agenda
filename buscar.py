# Importamos funciones y módulos.
from Listar import agenda
from colorama import Fore, Back

# Función para la busqueda de contacto por su nombre.
def buscar_contacto(nombre):
    if agenda == {}:
        print(Fore.WHITE + Back.RED +'No tenés ningún contacto en tu agenda')
    elif nombre in agenda.keys():
        print(Fore.GREEN +'Nombre:'+Fore.WHITE+ nombre, agenda[nombre])
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')
