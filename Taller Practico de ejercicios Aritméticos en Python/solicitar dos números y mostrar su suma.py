def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion

# 🔹 1. Definimos la función para calcular la suma de dos números
def sumar_numeros(numero1, numero2):
    # Fórmula: suma = número1 + número2
    suma = numero1 + numero2
    return suma  # Retornamos el resultado

# Lista para guardar los resultados
sumas = []


# 🔹 2. Definimos la función principal
def programa():
    print("Suma de dos números")
    
    # Pedimos los datos al usuario
    numero1 = float(input("Digita el primer número: "))
    numero2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función para calcular la suma
    resultado = sumar_numeros(numero1, numero2)
    
    # Mostramos el resultado
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
    
    # Guardamos el resultado en la lista
    sumas.append({"Numero1": numero1, "Numero2": numero2, "Resultado": resultado})


# 🔹 3. Función para ver los cálculos realizados
def ver_sumas():
    if not sumas:
        print("No hay sumas registradas.")
    else:
        print("\nLista de sumas calculadas:")
        for i, r in enumerate(sumas, start=1):
            print(f"{i}. Numero1: {r['Numero1']}, Numero2: {r['Numero2']}, Resultado: {r['Resultado']}")


# 🔹 4. Agregamos el menú CRUD para ejecutar las opciones
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


# 🔹 5. Llamamos la función principal para ejecutar el programa
ejecutar_menu()


