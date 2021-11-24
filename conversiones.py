# Importamos la agenda.
from Listar import agenda

# Función para pasar el diccionario a un archivo.
def diccionario_a_archivo():
    nombre_de_archivo = 'agenda.txt'
    archivo = open(nombre_de_archivo,'w')
    for nombre, dato in agenda.items():
        archivo.write(nombre+','+dato[0]+ ',' + dato[1]+'\n')
    archivo.close()


# Función que lee nuestro archivo txt.
def archivo_a_diccionario():
    nombre_de_archivo = 'agenda.txt'
    archivo = open(nombre_de_archivo,'r')
    lista_de_contactos = archivo.readlines()
    agenda.clear()
    for elemento in lista_de_contactos:
        agenda[elemento.strip().split(',')[0]]=elemento.strip().split(',')[1]
    archivo.close()
