def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de una pirámide
def calcular_volumen_piramide(longitud_base, ancho_base, altura):
    # Fórmula: V = (longitud_base × ancho_base × altura) / 3
    volumen = (longitud_base * ancho_base * altura) / 3
    return volumen


# Lista para guardar los resultados
piramides = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de una pirámide")
    
    # Pedimos los datos al usuario
    longitud_base = float(input("Digita la longitud de la base: "))
    ancho_base = float(input("Digita el ancho de la base: "))
    altura = float(input("Digita la altura de la pirámide: "))
    
    # Llamamos a la función calcular_volumen_piramide
    volumen = calcular_volumen_piramide(longitud_base, ancho_base, altura)
    
    # Mostramos el resultado
    print(f"El volumen de la pirámide es: {volumen}")
    
    # Guardamos el resultado en la lista
    piramides.append({"longitud_base": longitud_base, "ancho_base": ancho_base, "altura": altura, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_piramides():
    if not piramides:
        print("No hay pirámides registradas.")
    else:
        print("\nLista de pirámides calculadas:")
        for i, p in enumerate(piramides, start=1):
            print(f"{i}. Longitud base: {p['longitud_base']}, Ancho base: {p['ancho_base']}, Altura: {p['altura']}, Volumen: {p['volumen']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_piramides()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()