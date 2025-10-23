def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion

# 🔹 1. Definimos la función para calcular el volumen de un prisma rectangular
def calcular_volumen_prisma_rectangular(longitud, ancho, altura):
    # Fórmula: V = longitud × ancho × altura
    volumen = longitud * ancho * altura
    return volumen  # Retornamos el resultado

# Lista para guardar los resultados
volumenprisma = []


# 🔹 2. Definimos la función principal
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
    volumenprisma.append({"longitud": longitud, "ancho": ancho, "altura": altura})
    
# 🔹 3. Función para ver los cálculos realizados
def ver_prismas():
    if not volumenprisma:
        print("No hay rectángulos registrados.")
    else:
        print("\nLista de rectángulos calculados:")
        for i, r in enumerate(volumenprisma, start=1):
            print(f"{i}. Longitud: {r['longitud']}, Ancho: {r['ancho']}, Altura: {r['altura']}")


# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
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

# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()

