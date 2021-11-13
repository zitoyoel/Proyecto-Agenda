from colorama import init, Fore
init()
agenda = {} #diccionario vacío

def listar_directorio():
    #recorremos el diccionario y para cada llave, mostramos llave y valor
    for contacto,numero, email in agenda.items():
        print(Fore.YELLOW+contacto,' -- ',numero,' -- ',email)