def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion

import math  # ✅ 1. Importamos la librería para usar pi


# 🔹 2. Definimos la función para calcular el volumen de un cono
def calcular_volumen_cono(radio, altura):
    # Fórmula: V = (1/3) × π × r² × h
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    return volumen  # Retornamos el resultado

# Lista para guardar los resultados
volumencono = []


# 🔹 3. Definimos la función principal
def programa():
    print("Calcular el volumen de un cono")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la base del cono: "))
    altura = float(input("Digita la altura del cono: "))
    
    # Llamamos a la función calcular_volumen_cono
    volumen = calcular_volumen_cono(radio, altura)
    
    # Mostramos el resultado
    print(f"El volumen del cono es: {volumen}")
    
    # Guardamos el resultado en la lista
    volumencono.append({"radio": radio, "altura": altura})
    
# 🔹 3. Función para ver los cálculos realizados
def ver_volumencono():
    if not volumencono:
        print("No hay Volumenes registrados.")
    else:
        print("\nLista de Volumenes calculados:")
        for i, r in enumerate(volumencono, start=1):
            print(f"{i}. Radio: {r['radio']}, Altura: {r['altura']}")


# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_volumencono()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()
