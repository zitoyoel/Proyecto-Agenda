# Importamos funciones y módulos.
from Listar import agenda
from Conversiones import diccionario_a_archivo
from colorama import init, Fore, Back
init(autoreset=True)

# Función que agrega contacto por nombre, teléfono y email.
def agregar_contacto(nombre,telefono,email):
        agenda[nombre]=[telefono,email]
        print(Fore.WHITE + Back.GREEN +'Contacto agregado correctamente')
        diccionario_a_archivo()