def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el área de un hexágono regular
def calcular_area_hexagono(lado):
    # Fórmula: A = (3 × √3 × lado²) / 2
    import math
    area = (3 * math.sqrt(3) * (lado ** 2)) / 2
    return area


# Lista para guardar los resultados
hexagonos = []


# Definimos la función principal
def programa():
    print("Calcular el área de un hexágono regular")
    
    # Pedimos los datos al usuario
    lado = float(input("Digita la longitud del lado del hexágono: "))
    
    # Llamamos a la función calcular_area_hexagono
    area = calcular_area_hexagono(lado)
    
    # Mostramos el resultado
    print(f"El área del hexágono regular es: {area}")
    
    # Guardamos el resultado en la lista
    hexagonos.append({"lado": lado, "area": area})


# Función para ver los cálculos realizados
def ver_hexagonos():
    if not hexagonos:
        print("No hay hexágonos registrados.")
    else:
        print("\nLista de hexágonos calculados:")
        for i, h in enumerate(hexagonos, start=1):
            print(f"{i}. Lado: {h['lado']}, Área: {h['area']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_hexagonos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()