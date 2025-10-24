def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el área de un trapecio
def calcular_area_trapecio(base_mayor, base_menor, altura):
    # Fórmula: A = ((base_mayor + base_menor) / 2) × altura
    area = ((base_mayor + base_menor) / 2) * altura
    return area


# Lista para guardar los resultados
trapecios = []


# Definimos la función principal
def programa():
    print("Calcular el área de un trapecio")
    
    # Pedimos los datos al usuario
    base_mayor = float(input("Digita la base mayor del trapecio: "))
    base_menor = float(input("Digita la base menor del trapecio: "))
    altura = float(input("Digita la altura del trapecio: "))
    
    # Llamamos a la función calcular_area_trapecio
    area = calcular_area_trapecio(base_mayor, base_menor, altura)
    
    # Mostramos el resultado
    print(f"El área del trapecio es: {area}")
    
    # Guardamos el resultado en la lista
    trapecios.append({"base_mayor": base_mayor, "base_menor": base_menor, "altura": altura, "area": area})


# Función para ver los cálculos realizados
def ver_trapecios():
    if not trapecios:
        print("No hay trapecios registrados.")
    else:
        print("\nLista de trapecios calculados:")
        for i, t in enumerate(trapecios, start=1):
            print(f"{i}. Base mayor: {t['base_mayor']}, Base menor: {t['base_menor']}, Altura: {t['altura']}, Área: {t['area']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_trapecios()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()