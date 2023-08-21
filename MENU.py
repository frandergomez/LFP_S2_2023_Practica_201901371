print("******************************************************")
print("Practica1 - Lenguajes formales y de programación")
print("Nombre: Frander Oveldo Carreto Gómez")
print("Carné: 201901371")
print("Práctica#1")
print("******************************************************")
print("#Sistema de inventario:")
print("")

inventario = {}
# Función para actualizar el diccionario inventario
def actualizar_inventario():
    global inventario

# Función para cargar_inventario
def cargar_inventario():
    ruta = input("Ingrese la ruta del archivo: ")
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        print("Inventario cargado correctamente:")
        print(contenido)
    except FileNotFoundError:
        print("El archivo no se encontró.")
        print("")

# Función para cargar_instrucciones
def cargar_instrucciones():
    ruta = input("Ingrese la ruta del archivo de instrucciones: ")
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                procesar_instruccion(linea.strip())  # Elimina espacios y saltos de línea

        print("Instrucciones cargadas correctamente.")
    except FileNotFoundError:
        print("El archivo de instrucciones no se encontró.")

# Función para procesar_instruccion
def procesar_instruccion(instruccion):
    partes = instruccion.split(';')
    if partes[0] == 'agregar_stock':
        nombre = partes[1]
        cantidad = int(partes[2])
        ubicacion = partes[3]
        # Lógica para agregar stock
        print(f"Se agregó stock de {cantidad} unidades de {nombre} en {ubicacion}")
    elif partes[0] == 'vender_producto':
        nombre = partes[1]
        cantidad = int(partes[2])
        ubicacion = partes[3]
        # Lógica para vender producto
        print(f"Se vendieron {cantidad} unidades de {nombre} en {ubicacion}")
    else:
        print("Instrucción no reconocida:", instruccion)
    print("Instrucciones cargadas")
    print("")

# Función crear_informe_inventario
def crear_informe_inventario(inventario):
    nombre_archivo = "informe_inventario.txt"

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Informe de Inventario:\n")
            archivo.write("{:<20} {:<10} {:<15} {:<15} {}\n".format(
                "Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicación"))

            for producto, detalles in inventario.items():
                nombre = producto
                cantidad = detalles['cantidad']
                precio_unitario = detalles['precio_unitario']
                valor_total = cantidad * precio_unitario
                ubicacion = detalles['ubicacion']

                archivo.write("{:<20} {:<10} {:<15} {:<15} {}\n".format(
                    nombre, cantidad, precio_unitario, valor_total, ubicacion))

        print("Informe de inventario creado correctamente.")
    except Exception as e:
        print("Error al crear el informe de inventario:", str(e))

# Definición del diccionario inventario
inventario = {
    "Tomates": {"cantidad": 100, "precio_unitario": 1.0, "ubicacion": "BodegaA"},
    "Manzanas": {"cantidad": 250, "precio_unitario": 3.00, "ubicacion": "BodegaB"},
    "Peras":{"cantidad": 175, "precio_unitario":3.25, "ubicacion": "BodegaC"},
    "Platanos":{"cantidad": 75, "precio_unitario":1.75, "ubicacion": "BodegaD"},
    "Queso":{"cantidad":50, "precio_unitario":20.50, "ubicacion": "BodegaE"},
    "Helado":{"cantidad": 360, "precio_unitario":50, "ubicacion": "BodegaF"},
    "Arandanos":{"cantidad": 1000, "precio_unitario":0.50, "ubicacion": "BodegaG"},
    "Tomates":{"cantidad": 200, "precio_unitario":1.00, "ubicacion": "BodegaG"},
    "Manzanas":{"cantidad": 300, "precio_unitario":3.00, "ubicacion": "BodegaF"},
    "Peras":{"cantidad": 100, "precio_unitario":3.25, "ubicacion": "BodegaE"},
    "Platanos":{"cantidad": 50, "precio_unitario":1.75, "ubicacion": "BodegaC"},
    "Queso":{"cantidad": 10, "precio_unitario":20.50, "ubicacion": "BodegaD"},
    "Helado":{"cantidad": 80, "precio_unitario":6.50, "ubicacion": "BodegaB"},
    "Arandanos":{"cantidad": 5, "precio_unitario":0.50, "ubicacion": "BodegaA"},
}
# Función para el menú
while True:
    print("Menú:")
    print("1. Cargar inventario inicial")
    print("2. Cargar instrucciones de movimientos")
    print("3. Crear informe de inventario")
    print("4. Salir")
    print("")

    opcion = input("Seleccione una opción: ")
    print("")

    if opcion == '1':
        cargar_inventario()
    elif opcion == '2':
        cargar_instrucciones()
    elif opcion == '3':
        crear_informe_inventario(inventario)
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")