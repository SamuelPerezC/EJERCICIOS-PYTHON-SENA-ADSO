def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para sumar dos números
def sumar_numeros(num1, num2):
    # Fórmula: suma = número1 + número2
    suma = num1 + num2
    return suma


# Lista para guardar los resultados
sumas = []


# Definimos la función principal
def programa():
    print("Sumar dos números")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función sumar_numeros
    suma = sumar_numeros(num1, num2)
    
    # Mostramos el resultado
    print(f"La suma de {num1} + {num2} = {suma}")
    
    # Guardamos el resultado en la lista
    sumas.append({"num1": num1, "num2": num2, "suma": suma})


# Función para ver los cálculos realizados
def ver_sumas():
    if not sumas:
        print("No hay sumas registradas.")
    else:
        print("\nLista de sumas realizadas:")
        for i, s in enumerate(sumas, start=1):
            print(f"{i}. {s['num1']} + {s['num2']} = {s['suma']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_sumas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()