def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir Celsius a Fahrenheit
def convertir_celsius_fahrenheit(celsius):
    # Fórmula: F = (C × 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir Celsius a Fahrenheit")
    
    # Pedimos los datos al usuario
    celsius = float(input("Digita los grados Celsius: "))
    
    # Llamamos a la función convertir_celsius_fahrenheit
    fahrenheit = convertir_celsius_fahrenheit(celsius)
    
    # Mostramos el resultado
    print(f"{celsius}°C equivalen a {fahrenheit}°F")
    
    # Guardamos el resultado en la lista
    conversiones.append({"celsius": celsius, "fahrenheit": fahrenheit})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. {c['celsius']}°C = {c['fahrenheit']}°F")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_conversiones()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()