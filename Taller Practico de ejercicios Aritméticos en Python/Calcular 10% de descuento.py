def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el 10% de descuento
def calcular_descuento(precio):
    # Fórmula: descuento = precio × 0.10
    descuento = precio * 0.10
    return descuento


# Lista para guardar los resultados
descuentos = []


# Definimos la función principal
def programa():
    print("Calcular el 10% de descuento de un artículo")
    
    # Pedimos los datos al usuario
    precio = float(input("Digita el precio del artículo: "))
    
    # Llamamos a la función calcular_descuento
    descuento = calcular_descuento(precio)
    precio_final = precio - descuento
    
    # Mostramos el resultado
    print(f"Precio original: {precio}")
    print(f"Descuento (10%): {descuento}")
    print(f"Precio final: {precio_final}")
    
    # Guardamos el resultado en la lista
    descuentos.append({"precio": precio, "descuento": descuento, "precio_final": precio_final})


# Función para ver los cálculos realizados
def ver_descuentos():
    if not descuentos:
        print("No hay descuentos registrados.")
    else:
        print("\nLista de descuentos calculados:")
        for i, d in enumerate(descuentos, start=1):
            print(f"{i}. Precio: {d['precio']}, Descuento: {d['descuento']}, Precio final: {d['precio_final']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_descuentos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()