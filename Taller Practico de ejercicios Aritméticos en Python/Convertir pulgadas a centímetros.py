def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para convertir pulgadas a centímetros
def convertir_pulgadas_cm(pulgadas):
    # Fórmula: cm = pulgadas × 2.54
    centimetros = pulgadas * 2.54
    return centimetros


# Lista para guardar los resultados
conversiones = []


# Definimos la función principal
def programa():
    print("Convertir pulgadas a centímetros")
    
    # Pedimos los datos al usuario
    pulgadas = float(input("Digita la medida en pulgadas: "))
    
    # Llamamos a la función convertir_pulgadas_cm
    centimetros = convertir_pulgadas_cm(pulgadas)
    
    # Mostramos el resultado
    print(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros")
    
    # Guardamos el resultado en la lista
    conversiones.append({"pulgadas": pulgadas, "centimetros": centimetros})


# Función para ver los cálculos realizados
def ver_conversiones():
    if not conversiones:
        print("No hay conversiones registradas.")
    else:
        print("\nLista de conversiones realizadas:")
        for i, c in enumerate(conversiones, start=1):
            print(f"{i}. {c['pulgadas']} pulgadas = {c['centimetros']} cm")


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