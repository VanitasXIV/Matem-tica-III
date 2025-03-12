import re

def printMenu():
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Mostrar todos los clientes")
    print("5. Mostrar clientes preferentes")
    print("6. Cerrar programa")
    print("--------------------")
    
    
def validateEmail(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

def addClient(clientes):
    cuit = input("Ingrese el CUIT del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    
    while True:
        correo = input("Ingrese el correo del cliente: ")
        if validateEmail(correo):
            break
        else:
            print("Correo no válido. Intente de nuevo.")

    
    while True:
        preferente = input("¿Es cliente preferente? (s/n): ").lower()
        if preferente in ['s', 'n']:
            preferente = preferente == 's'
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")
    
    clientes[cuit] = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }
    print("Cliente añadido correctamente.")
    
    
def deleteClient(clientes):
    cuit = input("Ingrese el CUIT del cliente a eliminar: ")
    if cuit in clientes:
        del clientes[cuit]
        print("Cliente eliminado correctamente.")
    else:
        print("Cliente no encontrado.")

def searchClient(clientes):
    cuit = input("Ingrese el CUIT del cliente a mostrar: ")
    cliente = clientes.get(cuit)
    if cliente:
        print("\nDatos del cliente:")
        print(cliente)
    else:
        print("Cliente no encontrado.")

def listAllClients(clientes, preferentes=False):
    print("\n--- Lista de Clientes ---")
    for cuit, datos in clientes.items():
        if not preferentes or datos["preferente"]:
            print(f"CUIT: {cuit}, Nombre: {datos['nombre']}")
    if not clientes:
        print("No hay clientes registrados.")

def __main__():
    clientes = dict()
    print("Gestor de clientes")
    userInput = 0
    
    while userInput !=6:
        printMenu()
        userInput = int(input("Ingrese una opción válida: "))
        
        if userInput == 1:
            addClient(clientes)
        if userInput == 2:
            deleteClient(clientes)
        if userInput == 3:
            searchClient(clientes)
        if userInput == 4:
            listAllClients(clientes)
        if userInput == 5:
            listAllClients(clientes, True)
    
    print("Cerrando el programa...")
    quit()
    
__main__()
