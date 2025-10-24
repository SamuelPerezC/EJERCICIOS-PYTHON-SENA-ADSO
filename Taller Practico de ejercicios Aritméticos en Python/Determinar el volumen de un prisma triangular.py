def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el volumen de un prisma triangular
def calcular_volumen_prisma_triangular(longitud_base, altura_base, ancho):
    # Fórmula: V = (longitud_base × altura_base / 2) × ancho
    volumen = (longitud_base * altura_base / 2) * ancho
    return volumen


# Lista para guardar los resultados
prismas = []


# Definimos la función principal
def programa():
    print("Calcular el volumen de un prisma triangular")
    
    # Pedimos los datos al usuario
    longitud_base = float(input("Digita la longitud de la base del triángulo: "))
    altura_base = float(input("Digita la altura del triángulo: "))
    ancho = float(input("Digita el ancho del prisma: "))
    
    # Llamamos a la función calcular_volumen_prisma_triangular
    volumen = calcular_volumen_prisma_triangular(longitud_base, altura_base, ancho)
    
    # Mostramos el resultado
    print(f"El volumen del prisma triangular es: {volumen}")
    
    # Guardamos el resultado en la lista
    prismas.append({"longitud_base": longitud_base, "altura_base": altura_base, "ancho": ancho, "volumen": volumen})


# Función para ver los cálculos realizados
def ver_prismas():
    if not prismas:
        print("No hay prismas registrados.")
    else:
        print("\nLista de prismas calculados:")
        for i, p in enumerate(prismas, start=1):
            print(f"{i}. Longitud base: {p['longitud_base']}, Altura base: {p['altura_base']}, Ancho: {p['ancho']}, Volumen: {p['volumen']}")


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