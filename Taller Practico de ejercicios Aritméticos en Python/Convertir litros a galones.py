def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir litros a galones
def convertir_litros_galones(litros):
    # Fórmula: galones = litros × 0.264172
    galones = litros * 0.264172
    return galones


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir litros a galones")
    
    # Pedimos los datos al usuario
    litros = float(input("Digita el volumen en litros: "))
    
    # Llamamos a la función convertir_litros_galones
    galones = convertir_litros_galones(litros)
    
    # Mostramos el resultado
    print(f"{litros} litros equivalen a {galones} galones")
    
    # Guardamos el resultado en la lista
    conversiones.append({"litros": litros, "galones": galones})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. {c['litros']} litros = {c['galones']} galones")


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