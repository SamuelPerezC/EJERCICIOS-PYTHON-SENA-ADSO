def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    # Fórmula: A = (base × altura) / 2
    area = (base * altura) / 2
    return area


# Lista para guardar los resultados
triangulos = []


# Definimos la función principal
def programa():
    print("Calcular el área de un triángulo")
    
    # Pedimos los datos al usuario
    base = float(input("Digita la base del triángulo: "))
    altura = float(input("Digita la altura del triángulo: "))
    
    # Llamamos a la función calcular_area_triangulo
    area = calcular_area_triangulo(base, altura)
    
    # Mostramos el resultado
    print(f"El área del triángulo es: {area}")
    
    # Guardamos el resultado en la lista
    triangulos.append({"base": base, "altura": altura, "area": area})


# Función para ver los cálculos realizados
def ver_triangulos():
    if not triangulos:
        print("No hay triángulos registrados.")
    else:
        print("\nLista de triángulos calculados:")
        for i, t in enumerate(triangulos, start=1):
            print(f"{i}. Base: {t['base']}, Altura: {t['altura']}, Área: {t['area']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_triangulos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()