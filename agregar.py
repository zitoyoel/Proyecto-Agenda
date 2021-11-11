import os

nombre_archivo = 'agenda.txt'

agenda = dict()



def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('            AGREGAR CONTACTO')
    nombre = input('Nombre: ')
<<<<<<< HEAD
    if agenda.get(nombre):
        print('El contacto ya existe')
    else:
        telefono = input('Telefono: ')
        email = input('Mail: ')
    agenda.setdefault(nombre, (telefono, email))
=======
    telefono = input('Telefono: ')
    email = input('Mail: ')
    agenda.append([nombre, telefono, email])
>>>>>>> 66862a29de3f4e4f5d8aa98b3c6e0e5070a4ecfb
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f'nombre:{nombre}\ntelefono:{telefono}\nemail:{email}\n\n')
    os.system('cls')
    print('contacto agregado')



