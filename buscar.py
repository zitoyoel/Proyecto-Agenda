from listar import agenda

def buscar_contacto(nombre):
    if nombre in agenda.keys():
        print(nombre, '--', agenda[nombre])
    else:
        print('El nombre no se encuentra en el directorio')