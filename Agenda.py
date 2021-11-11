# from agregar import agregar_contacto
from agregar import agregar_contacto
from agregar import nombre_archivo
print('Bienvenido a su agenda de contactos \n1- Agregar contacto \n2- Buscar contacto \n3- Editar contacto \n4- Eliminar contacto')

agenda = []

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
                        print("error")
    except (ValueError):
        print("No es un dato válido")

print(agenda)