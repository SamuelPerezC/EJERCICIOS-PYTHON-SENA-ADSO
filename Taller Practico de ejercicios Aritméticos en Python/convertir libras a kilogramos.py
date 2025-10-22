# 🔹 1. Definimos la función para convertir libras a kilogramos
def convertir_libras_a_kilogramos(libras):
    # Fórmula: kilogramos = libras × 0.453592
    kilogramos = libras * 0.453592
    return kilogramos  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Convertir libras a kilogramos")
    
    # Pedimos los datos al usuario
    libras = float(input("Digita la cantidad en libras: "))
    
    # Llamamos a la función convertir_libras_a_kilogramos
    kilogramos = convertir_libras_a_kilogramos(libras)
    
    # Mostramos el resultado
    print(f"{libras} libras equivalen a {kilogramos} kilogramos")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
