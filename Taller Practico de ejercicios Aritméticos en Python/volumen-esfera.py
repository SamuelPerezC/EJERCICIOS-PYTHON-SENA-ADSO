import math  # Importamos la librería para usar pi

def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# 🔹 1. Definimos la función para calcular el volumen
def calcular_volumen_esfera(radio):
    # Fórmula: V=34​πr3
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen   # Retornamos el resultado

# Lista para guardar los resultados
volumenesfera = []


# 🔹 2. Definimos la función principal
def programa():
    print("Cálcular el volumen de una esfera")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la esfera: "))
    
    
    # Llamamos a la función calcular_volumen_esfera
    volumen = calcular_volumen_esfera(radio)
    
    # Mostramos el resultado
    print(f"El volumen de la esfera es: {volumen}")
    
    # Guardamos el resultado en la lista
    volumenesfera.append({"radio": radio})
    
# 🔹 3. Función para ver los cálculos realizados
def ver_volumen_esfera():
    if not volumenesfera:
        print("No hay volumenes registrados.")
    else:
        print("\nLista de volumenes calculados:")
        for i, r in enumerate(volumenesfera, start=1):
            print(f"{i}. radio: {r['radio']}")
            
# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_volumen_esfera()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()
