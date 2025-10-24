def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el residuo de la división
def calcular_residuo(num1, num2):
    # Fórmula: residuo = número1 % número2
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    residuo = num1 % num2
    return residuo


# Lista para guardar los resultados
residuos = []


# Definimos la función principal
def programa():
    print("Calcular el residuo de la división entre dos números")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función calcular_residuo
    residuo = calcular_residuo(num1, num2)
    
    # Mostramos el resultado
    if isinstance(residuo, str):
        print(residuo)
    else:
        print(f"El residuo de {num1} ÷ {num2} es: {residuo}")
    
    # Guardamos el resultado en la lista
    residuos.append({"num1": num1, "num2": num2, "residuo": residuo})


# Función para ver los cálculos realizados
def ver_residuos():
    if not residuos:
        print("No hay residuos registrados.")
    else:
        print("\nLista de residuos calculados:")
        for i, r in enumerate(residuos, start=1):
            if isinstance(r['residuo'], str):
                print(f"{i}. {r['num1']} % {r['num2']} = {r['residuo']}")
            else:
                print(f"{i}. {r['num1']} % {r['num2']} = {r['residuo']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_residuos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()