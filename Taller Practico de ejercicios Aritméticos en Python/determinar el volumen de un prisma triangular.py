def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion

# 🔹 1. Definimos la función para calcular el volumen del prisma triangular
def calcular_volumen_prisma_triangular(base, altura, ancho):
    # Fórmula: Volumen = (1/2 * base * altura) * ancho
    volumen = (0.5 * base * altura) * ancho
    return volumen  # Retornamos el resultado

# Lista para guardar los resultados
volumenprisma = []


# 🔹 2. Definimos la función principal
def programa():
    print("Determinar el volumen de un prisma triangular")
    
    # Pedimos los datos al usuario
    base = float(input("Digita la longitud de la base: "))
    altura = float(input("Digita la altura del triángulo: "))
    ancho = float(input("Digita el ancho del prisma: "))
    
    # Llamamos a la función para calcular el volumen
    volumen = calcular_volumen_prisma_triangular(base, altura, ancho)
    
    # Mostramos el resultado
    print(f"El volumen del prisma triangular es: {volumen}")
    # Guardamos el resultado en la lista
    volumenprisma.append({"base": base, "ancho": ancho, "altura": altura})


# 🔹 3. Función para ver los cálculos realizados
def ver_volumen():
    if not volumenprisma:
        print("No hay volumenes registrados.")
    else:
        print("\nLista de volumenes calculados:")
        for i, r in enumerate(volumenprisma, start=1):
            print(f"{i}. Base: {r['base']}, Ancho: {r['ancho']}, Altura: {r['altura']}")
            

# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_volumen()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            

# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()


