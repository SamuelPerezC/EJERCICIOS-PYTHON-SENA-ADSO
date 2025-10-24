def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el área de un círculo
def calcular_area_circulo(radio):
    # Fórmula: A = π × radio²
    import math
    area = math.pi * (radio ** 2)
    return area


# Lista para guardar los resultados
circulos = []


# Definimos la función principal
def programa():
    print("Calcular el área de un círculo")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio del círculo: "))
    
    # Llamamos a la función calcular_area_circulo
    area = calcular_area_circulo(radio)
    
    # Mostramos el resultado
    print(f"El área del círculo es: {area}")
    
    # Guardamos el resultado en la lista
    circulos.append({"radio": radio, "area": area})


# Función para ver los cálculos realizados
def ver_circulos():
    if not circulos:
        print("No hay círculos registrados.")
    else:
        print("\nLista de círculos calculados:")
        for i, c in enumerate(circulos, start=1):
            print(f"{i}. Radio: {c['radio']}, Área: {c['area']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_circulos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()