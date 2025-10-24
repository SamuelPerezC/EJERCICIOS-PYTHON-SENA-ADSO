def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular el promedio de dos números
def calcular_promedio(num1, num2):
    # Fórmula: promedio = (número1 + número2) / 2
    promedio = (num1 + num2) / 2
    return promedio


# Lista para guardar los resultados
promedios = []


# Definimos la función principal
def programa():
    print("Calcular el promedio de dos números")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función calcular_promedio
    promedio = calcular_promedio(num1, num2)
    
    # Mostramos el resultado
    print(f"El promedio de {num1} y {num2} es: {promedio}")
    
    # Guardamos el resultado en la lista
    promedios.append({"num1": num1, "num2": num2, "promedio": promedio})


# Función para ver los cálculos realizados
def ver_promedios():
    if not promedios:
        print("No hay promedios registrados.")
    else:
        print("\nLista de promedios calculados:")
        for i, p in enumerate(promedios, start=1):
            print(f"{i}. Promedio de {p['num1']} y {p['num2']} = {p['promedio']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_promedios()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()