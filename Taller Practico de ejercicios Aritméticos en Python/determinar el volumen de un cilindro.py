def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion

import math  # ✅ 1. Importamos la librería para usar pi


# 🔹 2. Definimos la función para calcular el volumen de un cilindro
def calcular_volumen_cilindro(radio, altura):
    # Fórmula: V = π × r² × h
    volumen = math.pi * (radio ** 2) * altura
    return volumen  # Retornamos el resultado

# Lista para guardar los resultados
volcilindro = []


# 🔹 3. Definimos la función principal
def programa():
    print("Calcular el volumen de un cilindro")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la base del cilindro: "))
    altura = float(input("Digita la altura del cilindro: "))
    
    # Llamamos a la función calcular_volumen_cilindro
    volumen = calcular_volumen_cilindro(radio, altura)
    
    # Mostramos el resultado
    print(f"El volumen del cilindro es: {volumen}")
    
    # Guardamos el resultado en la lista
    volcilindro.append({"radio": radio, "altura": altura})


# 🔹 3. Función para ver los cálculos realizados
def ver_volcilindro():
    if not volcilindro:
        print("No hay volumenes registrados.")
    else:
        print("\nLista de volumenes calculados:")
        for i, r in enumerate(volcilindro, start=1):
            print(f"{i}. Radio: {r['radio']}, Altura: {r['altura']}")


# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_volcilindro()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()

