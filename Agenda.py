import os
import pathlib
print('Bienvenido a su agenda de contactos \n1- Agregar contacto \n2- Buscar contacto \n3- Editar contacto \n4- Eliminar contacto')



agenda = {}


def agregar_contacto(agenda):
    os.system('cls')
    print('            AGREGAR CONTACTO')
    nombre = input('Nombre: ')
    if agenda.get(nombre):
        print('El contacto ya existe')
    else:
        telefono = input('Telefono: ')
        email = input('Mail: ')
        agenda.setdefault(nombre, telefono, email)
    os.system('cls')
    print('contacto agregado')



while True:
    try :
        opcion = int(input("Seleccione la opcion que desee: "))
        if opcion == 1:
            agregar_contacto(agenda)
            break
        else:
            if opcion == 2:
                print('Buscar contacto')
                break
            else:
                if opcion == 3:
                    print('Editar contacto')
                    break
                else:
                    if opcion == 4:
                        print('Eliminar contacto')
                        break
                    else:
                        print("error")
    except (ValueError):
        print("No es un dato válido")

print(agenda)