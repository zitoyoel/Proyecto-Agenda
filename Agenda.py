from listar import agenda
from listar import listar_directorio
from buscar import buscar_contacto
from conversiones import (diccionario_a_archivo, archivo_a_diccionario)
from colorama import init, Fore, Back, Style
init(autoreset=True)

def menu(): #mostramos el menu de opciones
    print('')
    print(Fore.MAGENTA+'------------------------')
    print(Fore.MAGENTA+ 'Agenda telefónica')
    print(Fore.MAGENTA+'------------------------')
    print(Fore.WHITE+'')
    print(Fore.CYAN+'1)' + Fore.WHITE+'Mostrar agenda')
    print(Fore.CYAN+'2)' + Fore.WHITE+ 'Agregar un contacto')
    print(Fore.CYAN+'3)' + Fore.WHITE+ 'Buscar contacto')
    print(Fore.CYAN+'4)' + Fore.WHITE+ 'Editar contacto')
    print(Fore.CYAN+'5)' + Fore.WHITE+ 'Eliminar contacto')
    print(Fore.RED+'0)' + Fore.WHITE+ 'Salir')
    print('')
    return(input('Ingrese la opción elegida: '))



def eliminar_contacto(nombre):
    if nombre in agenda.keys():
        del agenda[nombre]
        diccionario_a_archivo()
        print(Fore.WHITE + Back.GREEN +'Contacto eliminado')
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')


def modificar_contacto(nombre):
    if nombre in agenda.keys():
        print(nombre, agenda[nombre])
        nuevo_numero = input('Ingrese el nuevo telefono del contacto: ')
        nuevo_email = input('Agregue el nuevo email: ')
        agenda[nombre] = [nuevo_numero, nuevo_email]
        diccionario_a_archivo()
        print(Fore.WHITE + Back.GREEN +'Contacto modificado correctamente')
    else:
        print(Fore.WHITE + Back.RED +'El nombre no se encuentra en la agenda')

def agregar_contacto(nombre,telefono,email):
        agenda[nombre]=[telefono,email]
        print(Fore.WHITE + Back.GREEN +'contacto agregado correctamente')
        diccionario_a_archivo()


def programa():
    archivo_a_diccionario()

    while True:
        opcion = menu()
        if opcion == '0':
            print(Fore.WHITE + Back.RED +'Saliendo del directorio...')
            exit()
        elif opcion == '1':
            listar_directorio()
        elif opcion == '2':
            nombre = input('\nIngrese el nombre del contacto: ')
            if nombre in agenda.keys():
                print(Fore.WHITE + Back.RED +'El nombre ya existe')
            else:
                telefono = input('Ingrese el telefono del contacto: ')
                email = input('Ingrese el email del contacto: ')
                agregar_contacto(nombre,telefono,email)
        elif opcion == '3':
            nombre = input('Ingrese el nombre del contacto a buscar: ')
            buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input('Ingrese el nombre del contacto a modificar: ')
            modificar_contacto(nombre)
        elif opcion == '5':
            nombre = input('Ingrese el nombre del contacto a eliminar: ')
            eliminar_contacto(nombre)
        else:
            print(Fore.WHITE + Back.RED +'El numero ingresado no es valido')


programa() #Unica función que debemos llamar