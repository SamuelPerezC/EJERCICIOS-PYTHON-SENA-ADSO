def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de un cono
def calcular_volumen_cono(radio, altura):
    # Fórmula: V = (1/3) × π × radio² × altura
    import math
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    return volumen


# Lista para guardar los resultados
conos = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de un cono")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio del cono: "))
    altura = float(input("Digita la altura del cono: "))
    
    # Llamamos a la función calcular_volumen_cono
    volumen = calcular_volumen_cono(radio, altura)
    
    # Mostramos el resultado
    print(f"El volumen del cono es: {volumen}")
    
    # Guardamos el resultado en la lista
    conos.append({"radio": radio, "altura": altura, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_conos():
    if not conos:
        print("No hay conos registrados.")
    else:
        print("\nLista de conos calculados:")
        for i, c in enumerate(conos, start=1):
            print(f"{i}. Radio: {c['radio']}, Altura: {c['altura']}, Volumen: {c['volumen']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_conos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()