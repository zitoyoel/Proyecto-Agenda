# from agregar import agregar_contacto
from agregar import agregar_contacto
from agregar import nombre_archivo
from agregar import agenda
from listar import listar_directorio


print('Bienvenido a su agenda de contactos \n1- Agregar contacto \n2- Buscar contacto \n3- Editar contacto \n4- Eliminar contacto \n5- Mostrar Agenda')




while True:
    try :
        opcion = int(input("Seleccione la opcion que desee: "))
        if opcion == 1:
            agregar_contacto(agenda, nombre_archivo)
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
                        if opcion == 5:
                            listar_directorio()
                            break
                        else:
                            print("error")
    except (ValueError):
        print("No es un dato válido")
