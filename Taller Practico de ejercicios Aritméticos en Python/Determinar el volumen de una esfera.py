def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de una esfera
def calcular_volumen_esfera(radio):
    # Fórmula: V = (4/3) × π × radio³
    import math
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen


# Lista para guardar los resultados
esferas = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de una esfera")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la esfera: "))
    
    # Llamamos a la función calcular_volumen_esfera
    volumen = calcular_volumen_esfera(radio)
    
    # Mostramos el resultado
    print(f"El volumen de la esfera es: {volumen}")
    
    # Guardamos el resultado en la lista
    esferas.append({"radio": radio, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_esferas():
    if not esferas:
        print("No hay esferas registradas.")
    else:
        print("\nLista de esferas calculadas:")
        for i, e in enumerate(esferas, start=1):
            print(f"{i}. Radio: {e['radio']}, Volumen: {e['volumen']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_esferas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()