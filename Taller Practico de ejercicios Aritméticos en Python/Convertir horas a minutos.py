def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir horas a minutos
def convertir_horas_minutos(horas):
    # Fórmula: minutos = horas × 60
    minutos = horas * 60
    return minutos


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir horas a minutos")
    
    # Pedimos los datos al usuario
    horas = float(input("Digita la cantidad de horas: "))
    
    # Llamamos a la función convertir_horas_minutos
    minutos = convertir_horas_minutos(horas)
    
    # Mostramos el resultado
    print(f"{horas} horas equivalen a {minutos} minutos")
    
    # Guardamos el resultado en la lista
    conversiones.append({"horas": horas, "minutos": minutos})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. {c['horas']} horas = {c['minutos']} minutos")


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