from listar import agenda

def buscar_contacto(nombre,numero,email):
    if nombre in agenda.keys():
        print(nombre,'--',numero,'--',email)
    else:
        print('El nombre no se encuentra en el directorio')