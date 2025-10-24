def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el área de un paralelogramo
def calcular_area_paralelogramo(base, altura):
    # Fórmula: A = base × altura
    area = base * altura
    return area


# Lista para guardar los resultados
paralelogramos = []


# Definimos la función principal
def programa():
    print("Calcular el área de un paralelogramo")
    
    # Pedimos los datos al usuario
    base = float(input("Digita la base del paralelogramo: "))
    altura = float(input("Digita la altura del paralelogramo: "))
    
    # Llamamos a la función calcular_area_paralelogramo
    area = calcular_area_paralelogramo(base, altura)
    
    # Mostramos el resultado
    print(f"El área del paralelogramo es: {area}")
    
    # Guardamos el resultado en la lista
    paralelogramos.append({"base": base, "altura": altura, "area": area})


# Función para ver los cálculos realizados
def ver_paralelogramos():
    if not paralelogramos:
        print("No hay paralelogramos registrados.")
    else:
        print("\nLista de paralelogramos calculados:")
        for i, p in enumerate(paralelogramos, start=1):
            print(f"{i}. Base: {p['base']}, Altura: {p['altura']}, Área: {p['area']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_paralelogramos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()