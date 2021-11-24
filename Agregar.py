from Listar import agenda
from Conversiones import diccionario_a_archivo
from colorama import init, Fore, Back
init(autoreset=True)

def agregar_contacto(nombre,telefono,email):
        agenda[nombre]=[telefono,email]
        print(Fore.WHITE + Back.GREEN +'contacto agregado correctamente')
        diccionario_a_archivo()


