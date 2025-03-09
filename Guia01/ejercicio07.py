def mostrar_menu():
    print("\n--- MENÚ DE GESTIÓN DE CLIENTES ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")


def añadir_cliente(clientes):
    cuit = input("Ingrese el CUIT del cliente: ")
    if cuit in clientes:
        print("Ese CUIT ya está registrado.")
        return
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    preferente_input = input("¿Es cliente preferente? (s/n): ").strip().lower()
    preferente = preferente_input == 's'

    clientes[cuit] = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }
    print("Cliente añadido correctamente.")


def eliminar_cliente(clientes):
    cuit = input("Ingrese el CUIT del cliente a eliminar: ")
    if cuit in clientes:
        del clientes[cuit]
        print("Cliente eliminado correctamente.")
    else:
        print("No se encontró ningún cliente con ese CUIT.")


def mostrar_cliente(clientes):
    cuit = input("Ingrese el CUIT del cliente a mostrar: ")
    cliente = clientes.get(cuit)
    if cliente:
        print("\nDatos del cliente:")
        for clave, valor in cliente.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("Cliente no encontrado.")


def listar_todos(clientes):
    if not clientes:
        print("No hay clientes en la base de datos.")
    else:
        print("\nListado de todos los clientes:")
        for cuit, datos in clientes.items():
            print(f"CUIT: {cuit} - Nombre: {datos['nombre']}")


def listar_preferentes(clientes):
    preferentes = {cuit: datos for cuit, datos in clientes.items() if datos["preferente"]}
    if not preferentes:
        print("No hay clientes preferentes.")
    else:
        print("\nListado de clientes preferentes:")
        for cuit, datos in preferentes.items():
            print(f"CUIT: {cuit} - Nombre: {datos['nombre']}")


def main():
    clientes = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            añadir_cliente(clientes)
        elif opcion == '2':
            eliminar_cliente(clientes)
        elif opcion == '3':
            mostrar_cliente(clientes)
        elif opcion == '4':
            listar_todos(clientes)
        elif opcion == '5':
            listar_preferentes(clientes)
        elif opcion == '6':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
