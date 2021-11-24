# Importamos funciones y módulos.
from Listar import agenda;
from Conversiones import diccionario_a_archivo
from colorama import init, Fore, Back
init(autoreset=True)

# Función para eliminar un contacto por su nombre.
def eliminar_contacto(nombre):
    if agenda == {}:
        print(Fore.WHITE + Back.RED +'No tenes ningun contacto en tu agenda')
    elif nombre in agenda.keys():
        del agenda[nombre]
        diccionario_a_archivo()
        print(Fore.WHITE + Back.GREEN +'Contacto eliminado')
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')
