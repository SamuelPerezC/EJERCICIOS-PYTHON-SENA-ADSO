def menu():
    print("Menu")
    print("1. Crear")
    print("2. Ver")
    print("3. Salir")
    opcion = input("Opcion:")
    return opcion


# Definimos la función para calcular la raíz cuadrada
def calcular_raiz_cuadrada(numero):
    # Fórmula: raíz = número^(1/2)
    if numero < 0:
        return "Error: No se puede calcular raíz de número negativo"
    raiz = numero ** 0.5
    return raiz


# Lista para guardar los resultados
raices = []


# Definimos la función principal
def programa():
    print("Calcular la raíz cuadrada de un número")
    
    # Pedimos los datos al usuario
    numero = float(input("Digita el número: "))
    
    # Llamamos a la función calcular_raiz_cuadrada
    raiz = calcular_raiz_cuadrada(numero)
    
    # Mostramos el resultado
    if isinstance(raiz, str):
        print(raiz)
    else:
        print(f"La raíz cuadrada de {numero} es: {raiz}")
    
    # Guardamos el resultado en la lista
    raices.append({"numero": numero, "raiz": raiz})


# Función para ver los cálculos realizados
def ver_raices():
    if not raices:
        print("No hay raíces registradas.")
    else:
        print("\nLista de raíces calculadas:")
        for i, r in enumerate(raices, start=1):
            if isinstance(r['raiz'], str):
                print(f"{i}. √{r['numero']} = {r['raiz']}")
            else:
                print(f"{i}. √{r['numero']} = {r['raiz']}")


# Agregamos el menú para ejecutar las opciones
def ejecutar_menu():
    while True:
        opcion = menu()
        
        if opcion == "1":
            programa()
        elif opcion == "2":
            ver_raices()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Llamamos la función principal para ejecutar el programa
ejecutar_menu()