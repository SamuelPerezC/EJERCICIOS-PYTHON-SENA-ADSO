def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el cuadrado de un número
def calcular_cuadrado(numero):
    # Fórmula: cuadrado = número²
    cuadrado = numero ** 2
    return cuadrado


# Lista para guardar los resultados
cuadrados = []


# Definimos la función principal
def programa():
    print("Calcular el cuadrado de un número")
    
    # Pedimos los datos al usuario
    numero = float(input("Digita el número: "))
    
    # Llamamos a la función calcular_cuadrado
    cuadrado = calcular_cuadrado(numero)
    
    # Mostramos el resultado
    print(f"El cuadrado de {numero} es: {cuadrado}")
    
    # Guardamos el resultado en la lista
    cuadrados.append({"numero": numero, "cuadrado": cuadrado})


# Función para ver los cálculos realizados
def ver_cuadrados():
    if not cuadrados:
        print("No hay cuadrados registrados.")
    else:
        print("\nLista de cuadrados calculados:")
        for i, c in enumerate(cuadrados, start=1):
            print(f"{i}. {c['numero']}² = {c['cuadrado']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_cuadrados()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()