def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para determinar si un número es par o impar
def determinar_par_impar(numero):
    # Fórmula: si número % 2 == 0 entonces es par, sino es impar
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"


# Lista para guardar los resultados
numeros = []


# Definimos la función principal
def programa():
    print("Determinar si un número es par o impar")
    
    # Pedimos los datos al usuario
    numero = int(input("Digita el número: "))
    
    # Llamamos a la función determinar_par_impar
    resultado = determinar_par_impar(numero)
    
    # Mostramos el resultado
    print(f"El número {numero} es {resultado}")
    
    # Guardamos el resultado en la lista
    numeros.append({"numero": numero, "resultado": resultado})


# Función para ver los cálculos realizados
def ver_numeros():
    if not numeros:
        print("No hay números registrados.")
    else:
        print("\nLista de números analizados:")
        for i, n in enumerate(numeros, start=1):
            print(f"{i}. {n['numero']} es {n['resultado']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_numeros()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()