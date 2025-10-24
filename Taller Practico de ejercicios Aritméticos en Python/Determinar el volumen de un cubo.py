def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de un cubo
def calcular_volumen_cubo(lado):
    # Fórmula: V = lado³
    volumen = lado ** 3
    return volumen


# Lista para guardar los resultados
cubos = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de un cubo")
    
    # Pedimos los datos al usuario
    lado = float(input("Digita la longitud del lado del cubo: "))
    
    # Llamamos a la función calcular_volumen_cubo
    volumen = calcular_volumen_cubo(lado)
    
    # Mostramos el resultado
    print(f"El volumen del cubo es: {volumen}")
    
    # Guardamos el resultado en la lista
    cubos.append({"lado": lado, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_cubos():
    if not cubos:
        print("No hay cubos registrados.")
    else:
        print("\nLista de cubos calculados:")
        for i, c in enumerate(cubos, start=1):
            print(f"{i}. Lado: {c['lado']}, Volumen: {c['volumen']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_cubos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()