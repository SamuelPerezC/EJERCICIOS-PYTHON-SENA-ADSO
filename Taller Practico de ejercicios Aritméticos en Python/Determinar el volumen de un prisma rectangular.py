def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de un prisma rectangular
def calcular_volumen_prisma_rectangular(longitud, ancho, altura):
    # Fórmula: V = longitud × ancho × altura
    volumen = longitud * ancho * altura
    return volumen


# Lista para guardar los resultados
prismas = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de un prisma rectangular")
    
    # Pedimos los datos al usuario
    longitud = float(input("Digita la longitud del prisma: "))
    ancho = float(input("Digita el ancho del prisma: "))
    altura = float(input("Digita la altura del prisma: "))
    
    # Llamamos a la función calcular_volumen_prisma_rectangular
    volumen = calcular_volumen_prisma_rectangular(longitud, ancho, altura)
    
    # Mostramos el resultado
    print(f"El volumen del prisma rectangular es: {volumen}")
    
    # Guardamos el resultado en la lista
    prismas.append({"longitud": longitud, "ancho": ancho, "altura": altura, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_prismas():
    if not prismas:
        print("No hay prismas registrados.")
    else:
        print("\nLista de prismas calculados:")
        for i, p in enumerate(prismas, start=1):
            print(f"{i}. Longitud: {p['longitud']}, Ancho: {p['ancho']}, Altura: {p['altura']}, Volumen: {p['volumen']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_prismas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()