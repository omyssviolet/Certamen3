#Parámetros importantes

from os import system
import csv
import random
system("cls") #Limpiar

pedidos = []
comunas = ["concepcion", "chiguayante", "talcahuano", "hualpen", "san pedro"]

#Función MENÚ
def menu():
    system("cls") #Limpiar
    print("####### CleanWasser #######")
    print("\n1) Registrar pedido\n2) Listar todo los pedidos\n3) Imprimir hoja de ruta\n4) Buscar pedido por ID\n5) Salir\n ")

#Función para registrar pedidos
def registrar_pedido():
    system("cls") #Limpiar
    print("####### Registrar Pedido #######\n")

    while True:
        nombre_cliente = input("Ingrese nombre del cliente: ")
        if nombre_cliente == "":
            print("El campo no puede estar vacío. Por favor, ingrese nuevamente...")
        elif nombre_cliente.isalpha():
            break
        else:
            print("El nombre no puede ser un número")

    while True:
        apellido_cliente = input("Ingrese apellido del cliente: ")
        if apellido_cliente == "":
            print("El campo no puede estar vacío. Por favor, ingrese nuevamente")
        elif apellido_cliente.isalpha():
            break
        else:
            print("El nombre no puede ser un número")

    while True:
        system("cls") #Limpiar
        print("\nComunas disponibles\n.- Concepción\n.- Chiguayante\n.- Talcahuano\n.- Hualpén\n.- San Pedro\n")
        comuna_cliente = input("Ingrese comuna del cliente: ").strip().lower()
        if comuna_cliente not in comunas:
            input("Comuna ingresada no es válida. Presione ENTER para continuar... ")
        else:
            break
    
    while True:
        direccion = input("\nIngrese la dirección del pedido: ")
        if direccion == "":
            print("La dirección no puede estar vacía")
        else:
            break

    dispensador_6lt = 0
    dispensador_10lt = 0
    dispensador_20lt = 0

    while True:
        system("cls") #Limpiar
        print("####### Detalle de Pedido #######\n1) Disp. 6 Litros\n2) Disp. 10 Litros\n3) Disp. 20 Litros\n4) Salir")
        dispensador_cliente = input("Ingrese dispensador del Cliente: ")

        if dispensador_cliente == "1":
            print("¿Cuántos dispensadores desea ingresar?")
            try:
                dispensador_6lt = int(input("Ingrese cantidad: "))
            except ValueError:
                print("La cantidad debe ser un número entero. Por favor, intente nuevamente...")

        elif dispensador_cliente == "2":
            print("¿Cuántos dispensadores desea ingresar?")
            try:
                dispensador_10lt = int(input("Ingrese cantidad: "))
            except ValueError:
                print("La cantidad debe ser un número entero. Por favor, intente nuevamente...")

        elif dispensador_cliente == "3":
            print("¿Cuántos dispensadores desea ingresar?")
            try:
                dispensador_20lt = int(input("Ingrese cantidad: "))
            except ValueError:
                print("La cantidad debe ser un número entero. Por favor, intente nuevamente...")
        elif dispensador_cliente == "4":
            print("Salir del registro")
            break
        else:
            print("Opción ingresada no es válida")

    numero_aleatorio = random.randint(1000,9999)
    id = numero_aleatorio

    pedido = {
        "id": id,
        "nombre": nombre_cliente,
        "apellido": apellido_cliente,
        "direccion": direccion,
        "comuna": comuna_cliente,
        "Disp.6lts": dispensador_6lt,
        "Disp.10lts": dispensador_10lt,
        "Disp.20lts": dispensador_20lt
        }
    pedidos.append(pedido)

# Función para imprimir hoja de ruta
def listar_pedidos():
    if not pedidos:
        input("No hay pedidos registrados\nPresione ENTER para continuar")
        return
    
    encabezados = ["id", "nombre", "apellido", "direccion", "comuna", "Disp.6lts", "Disp.10lts", "Disp.20lts"]

    data = [encabezados]
    for pedido in pedidos:
        fila = [
            pedido["id"],
            pedido["nombre"],
            pedido["apellido"],
            pedido["direccion"],
            pedido["comuna"],
            pedido["Disp.6lts"],
            pedido["Disp.10lts"],
            pedido["Disp.20lts"]
        ]
        data.append(fila)
    
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    
    def print_row(row):
        print("|", end=" ")
        for item, width in zip(row, column_widths):
            print(f"{str(item):<{width}}", end=" | ")
        print()

    print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))

    print_row(data[0])

    print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))

    for row in data[1:]:
        print_row(row)

    print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))

    input("Presione enter para continuar... ")

# Función para imprimir hoja de ruta
def imprimir_Hruta():

    system("cls")#Limpiar
    print("####### Imprimir Hoja de Ruta #######\nComunas Disponibles")
    for i, comuna_cliente in enumerate(comunas, start=1):
        print(f"{i}. {comuna_cliente}")
    try:
        seleccion = int(input("Seleccone opción: "))
    except ValueError:
        print("Opción no válida. Por favor, intente nuevamente...")

    comuna_seleccionada =comunas[seleccion - 1]

    archivo_csv = f"hoja_de_ruta_{comuna_seleccionada}.csv"
    try:
        with open(archivo_csv, mode="w", newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["id", "nombre", "apellido", "direccion", "comuna", "Disp.6lts", "Disp.10lts", "Disp.20lts"])

            for pedido in pedidos:
                if pedido ["comuna"] == comuna_seleccionada:
                    writer.writerow([pedido["id"],
                                     pedido["nombre"], 
                                     pedido["apellido"], 
                                     pedido["direccion"], 
                                     pedido["comuna"],
                                     pedido["Disp.6lts"],
                                     pedido["Disp.10lts"],
                                     pedido["Disp.20lts"]]
                                     )
                    print(f"\nArchivo '{archivo_csv}' generado exitosamente.")
    except IOError:
        print("Ocurrió un error al escribir el archivo CSV.")
    input("\nPresione ENTER para continuar")

#Función para buscar pedidos por ID
def buscar_ID():
    print("####### BUSCAR PEDIDO POR ID #######")
    try:
        id = int(input("Ingrese el ID del pedido => "))
    except ValueError:
        input("El ID debe ser un número entero.\nPresione ENTER para continuar... ")
        return
    for pedido in pedidos:
        if pedido["id"] == id:
            print(f"Pedido encontrado: {pedido}")

while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_pedido()
    elif opcion == "2":
        listar_pedidos()
    elif opcion == "3":
        imprimir_Hruta()
    elif opcion == "4":
     buscar_ID()
    elif opcion == "5":
        print("Saliendo del programa...")
        break