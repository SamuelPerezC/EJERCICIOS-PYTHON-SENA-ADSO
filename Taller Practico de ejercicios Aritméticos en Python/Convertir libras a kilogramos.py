def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir libras a kilogramos
def convertir_libras_kg(libras):
    # Fórmula: kg = libras × 0.453592
    kilogramos = libras * 0.453592
    return kilogramos


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir libras a kilogramos")
    
    # Pedimos los datos al usuario
    libras = float(input("Digita el peso en libras: "))
    
    # Llamamos a la función convertir_libras_kg
    kilogramos = convertir_libras_kg(libras)
    
    # Mostramos el resultado
    print(f"{libras} libras equivalen a {kilogramos} kilogramos")
    
    # Guardamos el resultado en la lista
    conversiones.append({"libras": libras, "kilogramos": kilogramos})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. {c['libras']} libras = {c['kilogramos']} kg")


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