def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir dólares a euros
def convertir_dolares_euros(dolares, tasa_cambio=0.85):
    # Fórmula: euros = dólares × tasa_de_cambio
    euros = dolares * tasa_cambio
    return euros


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir dólares a euros")
    
    # Pedimos los datos al usuario
    dolares = float(input("Digita la cantidad en dólares: "))
    tasa = input("Digita la tasa de cambio (presiona Enter para usar 0.85 por defecto): ")
    
    if tasa == "":
        tasa = 0.85
    else:
        tasa = float(tasa)
    
    # Llamamos a la función convertir_dolares_euros
    euros = convertir_dolares_euros(dolares, tasa)
    
    # Mostramos el resultado
    print(f"${dolares} USD equivalen a €{euros} EUR")
    
    # Guardamos el resultado en la lista
    conversiones.append({"dolares": dolares, "tasa": tasa, "euros": euros})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. ${c['dolares']} USD = €{c['euros']} EUR (tasa: {c['tasa']})")


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