from colorama import init, Fore, Back
init()
agenda = {} #diccionario vacío



def listar_agenda():
    if agenda == {}:
        print(Fore.WHITE + Back.RED +'No tenes ningun contacto en tu agenda')
#recorremos el diccionario y para cada llave, mostramos llave y valor
    for nombre, dato in agenda.items():
        print(Fore.GREEN +'Nombre:'+Fore.WHITE+ nombre +Fore.GREEN + ' Telefono:'+Fore.WHITE+ dato[0] +Fore.GREEN +' Email:'+ Fore.WHITE+dato[1])