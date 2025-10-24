def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el 5% de interés
def calcular_interes(cantidad):
    # Fórmula: interés = cantidad × 0.05
    interes = cantidad * 0.05
    return interes


# Lista para guardar los resultados
intereses = []


# Definimos la función principal
def programa():
    print("Calcular el 5% de interés de una cuenta")
    
    # Pedimos los datos al usuario
    cantidad = float(input("Digita la cantidad de dinero en la cuenta: "))
    
    # Llamamos a la función calcular_interes
    interes = calcular_interes(cantidad)
    total = cantidad + interes
    
    # Mostramos el resultado
    print(f"Cantidad inicial: {cantidad}")
    print(f"Interés (5%): {interes}")
    print(f"Total con interés: {total}")
    
    # Guardamos el resultado en la lista
    intereses.append({"cantidad": cantidad, "interes": interes, "total": total})


# Función para ver los cálculos realizados
def ver_intereses():
    if not intereses:
        print("No hay intereses registrados.")
    else:
        print("\nLista de intereses calculados:")
        for i, i_val in enumerate(intereses, start=1):
            print(f"{i}. Cantidad: {i_val['cantidad']}, Interés: {i_val['interes']}, Total: {i_val['total']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_intereses()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()