def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de un cilindro
def calcular_volumen_cilindro(radio, altura):
    # Fórmula: V = π × radio² × altura
    import math
    volumen = math.pi * (radio ** 2) * altura
    return volumen


# Lista para guardar los resultados
cilindros = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de un cilindro")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio del cilindro: "))
    altura = float(input("Digita la altura del cilindro: "))
    
    # Llamamos a la función calcular_volumen_cilindro
    volumen = calcular_volumen_cilindro(radio, altura)
    
    # Mostramos el resultado
    print(f"El volumen del cilindro es: {volumen}")
    
    # Guardamos el resultado en la lista
    cilindros.append({"radio": radio, "altura": altura, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_cilindros():
    if not cilindros:
        print("No hay cilindros registrados.")
    else:
        print("\nLista de cilindros calculados:")
        for i, c in enumerate(cilindros, start=1):
            print(f"{i}. Radio: {c['radio']}, Altura: {c['altura']}, Volumen: {c['volumen']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_cilindros()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()