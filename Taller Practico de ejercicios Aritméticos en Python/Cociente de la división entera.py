def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el cociente de la división entera
def calcular_cociente_entero(num1, num2):
    # Fórmula: cociente = número1 // número2
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    cociente = num1 // num2
    return cociente


# Lista para guardar los resultados
cocientes = []


# Definimos la función principal
def programa():
    print("Calcular el cociente de la división entera")
    
    # Pedimos los datos al usuario
    num1 = int(input("Digita el primer número entero: "))
    num2 = int(input("Digita el segundo número entero: "))
    
    # Llamamos a la función calcular_cociente_entero
    cociente = calcular_cociente_entero(num1, num2)
    
    # Mostramos el resultado
    if isinstance(cociente, str):
        print(cociente)
    else:
        print(f"El cociente entero de {num1} ÷ {num2} es: {cociente}")
    
    # Guardamos el resultado en la lista
    cocientes.append({"num1": num1, "num2": num2, "cociente": cociente})


# Función para ver los cálculos realizados
def ver_cocientes():
    if not cocientes:
        print("No hay cocientes registrados.")
    else:
        print("\nLista de cocientes calculados:")
        for i, c in enumerate(cocientes, start=1):
            if isinstance(c['cociente'], str):
                print(f"{i}. {c['num1']} // {c['num2']} = {c['cociente']}")
            else:
                print(f"{i}. {c['num1']} // {c['num2']} = {c['cociente']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_cocientes()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()