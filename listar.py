from colorama import init, Fore
init()
agenda = {} #diccionario vacío

def listar_directorio():
    #recorremos el diccionario y para cada llave, mostramos llave y valor
    for nombre, dato in agenda.items():
        print(Fore.GREEN +'Nombre:'+Fore.WHITE+ nombre +Fore.GREEN + ' Telefono:'+Fore.WHITE+ dato[0] +Fore.GREEN +' Email:'+ Fore.WHITE+dato[1])