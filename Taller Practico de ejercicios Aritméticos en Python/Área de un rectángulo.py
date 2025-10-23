def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# 🔹 1. Definimos la función para calcular el área de un rectángulo
def calcular_area_rectangulo(longitud, ancho):
    # Fórmula: A = longitud × ancho
    area = longitud * ancho
    return area  # Retornamos el resultado


# Lista para guardar los resultados
rectangulos = []


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el área de un rectángulo")
    
    # Pedimos los datos al usuario
    longitud = float(input("Digita la longitud del rectángulo: "))
    ancho = float(input("Digita el ancho del rectángulo: "))
    
    # Llamamos a la función calcular_area_rectangulo
    area = calcular_area_rectangulo(longitud, ancho)
    
    # Mostramos el resultado
    print(f"El área del rectángulo es: {area}")
    
    # Guardamos el resultado en la lista
    rectangulos.append({"longitud": longitud, "ancho": ancho, "area": area})


# 🔹 3. Función para ver los cálculos realizados
def ver_rectangulos():
    if not rectangulos:
        print("No hay rectángulos registrados.")
    else:
        print("\nLista de rectángulos calculados:")
        for i, r in enumerate(rectangulos, start=1):
            print(f"{i}. Longitud: {r['longitud']}, Ancho: {r['ancho']}, Área: {r['area']}")


# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_rectangulos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()

