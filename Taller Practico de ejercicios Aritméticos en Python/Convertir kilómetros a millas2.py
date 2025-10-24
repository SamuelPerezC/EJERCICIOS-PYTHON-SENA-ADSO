def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir kilómetros a millas
def convertir_km_millas(kilometros):
    # Fórmula: millas = kilómetros × 0.621371
    millas = kilometros * 0.621371
    return millas


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir kilómetros a millas")
    
    # Pedimos los datos al usuario
    kilometros = float(input("Digita la distancia en kilómetros: "))
    
    # Llamamos a la función convertir_km_millas
    millas = convertir_km_millas(kilometros)
    
    # Mostramos el resultado
    print(f"{kilometros} km equivalen a {millas} millas")
    
    # Guardamos el resultado en la lista
    conversiones.append({"kilometros": kilometros, "millas": millas})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. {c['kilometros']} km = {c['millas']} millas")


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