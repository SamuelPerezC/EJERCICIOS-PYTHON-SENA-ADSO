def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular la circunferencia de un círculo
def calcular_circunferencia(radio):
    # Fórmula: C = 2 × π × radio
    import math
    circunferencia = 2 * math.pi * radio
    return circunferencia


# Lista para guardar los resultados
circunferencias = []


# Definimos la función principal
def programa():
    print("Calcular la circunferencia de un círculo")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio del círculo: "))
    
    # Llamamos a la función calcular_circunferencia
    circunferencia = calcular_circunferencia(radio)
    
    # Mostramos el resultado
    print(f"La circunferencia del círculo es: {circunferencia}")
    
    # Guardamos el resultado en la lista
    circunferencias.append({"radio": radio, "circunferencia": circunferencia})


# Función para ver los cálculos realizados
def ver_circunferencias():
    if not circunferencias:
        print("No hay circunferencias registradas.")
    else:
        print("\nLista de circunferencias calculadas:")
        for i, c in enumerate(circunferencias, start=1):
            print(f"{i}. Radio: {c['radio']}, Circunferencia: {c['circunferencia']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_circunferencias()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()