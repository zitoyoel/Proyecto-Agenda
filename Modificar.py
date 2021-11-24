# Importamos funciones y módulos.
from Listar import agenda
from Conversiones import diccionario_a_archivo
from colorama import init, Fore, Back
init(autoreset=True)

# Función para modificar teléfono y email del contacto por su nombre.
def modificar_contacto(nombre):
    if agenda == {}:
        print(Fore.WHITE + Back.RED +'No tenés ningún contacto en tu agenda')
    elif nombre in agenda.keys():
        print(nombre, agenda[nombre])
        nuevo_numero = input('Ingrese el nuevo teléfono del contacto: ')
        nuevo_email = input('Agregue el nuevo email: ')
        agenda[nombre] = [nuevo_numero, nuevo_email]
        diccionario_a_archivo()
        print(Fore.WHITE + Back.GREEN +'Contacto modificado correctamente')
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')
