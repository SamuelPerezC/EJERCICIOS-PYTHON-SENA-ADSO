def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para determinar si un número es múltiplo de otro
def es_multiplo(num1, num2):
    # Fórmula: si número1 % número2 == 0 entonces es múltiplo
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    if num1 % num2 == 0:
        return f"{num1} es múltiplo de {num2}"
    else:
        return f"{num1} no es múltiplo de {num2}"


# Lista para guardar los resultados
multiplos = []


# Definimos la función principal
def programa():
    print("Determinar si un número es múltiplo de otro")
    
    # Pedimos los datos al usuario
    num1 = float(input("Digita el primer número: "))
    num2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función es_multiplo
    resultado = es_multiplo(num1, num2)
    
    # Mostramos el resultado
    print(resultado)
    
    # Guardamos el resultado en la lista
    multiplos.append({"num1": num1, "num2": num2, "resultado": resultado})


# Función para ver los cálculos realizados
def ver_multiplos():
    if not multiplos:
        print("No hay múltiplos registrados.")
    else:
        print("\nLista de múltiplos analizados:")
        for i, m in enumerate(multiplos, start=1):
            print(f"{i}. {m['resultado']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_multiplos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()