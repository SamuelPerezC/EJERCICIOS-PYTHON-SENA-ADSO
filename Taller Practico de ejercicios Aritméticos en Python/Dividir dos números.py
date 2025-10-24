def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para dividir dos números
def dividir_numeros(num1, num2):
    # Fórmula: división = número1 ÷ número2
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    division = num1 / num2
    return division


# Lista para guardar los resultados
divisiones = []


# Definimos la función principal
def programa():
    print("Dividir dos números")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función dividir_numeros
    division = dividir_numeros(num1, num2)
    
    # Mostramos el resultado
    if isinstance(division, str):
        print(division)
    else:
        print(f"La división de {num1} ÷ {num2} = {division}")
    
    # Guardamos el resultado en la lista
    divisiones.append({"num1": num1, "num2": num2, "division": division})


# Función para ver los cálculos realizados
def ver_divisiones():
    if not divisiones:
        print("No hay divisiones registradas.")
    else:
        print("\nLista de divisiones realizadas:")
        for i, d in enumerate(divisiones, start=1):
            if isinstance(d['division'], str):
                print(f"{i}. {d['num1']} ÷ {d['num2']} = {d['division']}")
            else:
                print(f"{i}. {d['num1']} ÷ {d['num2']} = {d['division']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_divisiones()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()