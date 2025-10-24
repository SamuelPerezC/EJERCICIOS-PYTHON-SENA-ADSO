def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para multiplicar dos números
def multiplicar_numeros(num1, num2):
    # Fórmula: producto = número1 × número2
    producto = num1 * num2
    return producto


# Lista para guardar los resultados
multiplicaciones = []


# Definimos la función principal
def programa():
    print("Multiplicar dos números")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función multiplicar_numeros
    producto = multiplicar_numeros(num1, num2)
    
    # Mostramos el resultado
    print(f"El producto de {num1} × {num2} = {producto}")
    
    # Guardamos el resultado en la lista
    multiplicaciones.append({"num1": num1, "num2": num2, "producto": producto})


# Función para ver los cálculos realizados
def ver_multiplicaciones():
    if not multiplicaciones:
        print("No hay multiplicaciones registradas.")
    else:
        print("\nLista de multiplicaciones realizadas:")
        for i, m in enumerate(multiplicaciones, start=1):
            print(f"{i}. {m['num1']} × {m['num2']} = {m['producto']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_multiplicaciones()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()