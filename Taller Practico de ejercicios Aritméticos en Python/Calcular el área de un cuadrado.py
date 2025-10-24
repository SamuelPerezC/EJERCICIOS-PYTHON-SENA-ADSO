def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    # Fórmula: A = lado²
    area = lado ** 2
    return area


# Lista para guardar los resultados
cuadrados = []


# Definimos la función principal
def programa():
    print("Calcular el área de un cuadrado")
    
    # Pedimos los datos al usuario
    lado = float(input("Digita el lado del cuadrado: "))
    
    # Llamamos a la función calcular_area_cuadrado
    area = calcular_area_cuadrado(lado)
    
    # Mostramos el resultado
    print(f"El área del cuadrado es: {area}")
    
    # Guardamos el resultado en la lista
    cuadrados.append({"lado": lado, "area": area})


# Función para ver los cálculos realizados
def ver_cuadrados():
    if not cuadrados:
        print("No hay cuadrados registrados.")
    else:
        print("\nLista de cuadrados calculados:")
        for i, c in enumerate(cuadrados, start=1):
            print(f"{i}. Lado: {c['lado']}, Área: {c['area']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_cuadrados()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()