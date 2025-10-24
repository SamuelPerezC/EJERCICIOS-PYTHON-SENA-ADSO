def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para restar dos números
def restar_numeros(num1, num2):
    # Fórmula: resta = número1 - número2
    resta = num1 - num2
    return resta


# Lista para guardar los resultados
restas = []


# Definimos la función principal
def programa():
    print("Restar dos números")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función restar_numeros
    resta = restar_numeros(num1, num2)
    
    # Mostramos el resultado
    print(f"La resta de {num1} - {num2} = {resta}")
    
    # Guardamos el resultado en la lista
    restas.append({"num1": num1, "num2": num2, "resta": resta})


# Función para ver los cálculos realizados
def ver_restas():
    if not restas:
        print("No hay restas registradas.")
    else:
        print("\nLista de restas realizadas:")
        for i, r in enumerate(restas, start=1):
            print(f"{i}. {r['num1']} - {r['num2']} = {r['resta']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_restas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()