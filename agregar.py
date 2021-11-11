
import os

nombre_archivo = 'agenda.txt'

def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('            AGREGAR CONTACTO')
    nombre = input('Nombre: ')
    telefono = input('Telefono: ')
    email = input('Mail: ')
    agenda.count(nombre) != 0
    print('El contacto ya existe')
    agenda.append([nombre, telefono, email])
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f'nombre:{nombre}\ntelefono:{telefono}\nemail:{email}\n \n')
    os.system('cls')
    print('contacto agregado')


