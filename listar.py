from agregar import agenda

def diccionario_a_archivo():
    nombre_de_archivo = 'agenda.txt'
    archivo = open(nombre_de_archivo,'w')
    for nombre,telefono, email in agenda.items():
        archivo.write(f'{nombre},{telefono}, {email} ')
    archivo.close()

def archivo_a_diccionario(): #leemos el directorio del archivo de disco
    nombre_de_archivo = 'agenda.txt'
    archivo = open(nombre_de_archivo,'r')
    lista_de_contactos = archivo.readlines() #leo todo el directorio con una lista
    #un elemento en la lista por cada renglon del txt
    agenda.clear() #Limpiamos el diccionario
    for elemento in lista_de_contactos:
        print( elemento.strip().split(',')[0],elemento.strip().split(',')[1] )
        agenda[elemento.strip().split(',')[0]]=elemento.strip().split(',')[1]
    archivo.close()

def listar_directorio():
    #recorremos el diccionario y para cada llave, mostramos llave y valor
    for nombre,telefono, email in agenda.items():
        print(nombre,' -- ',telefono, ' -- ', email)