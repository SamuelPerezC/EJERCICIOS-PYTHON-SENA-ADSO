# 🔹 1. Definimos la función para convertir kilómetros a millas
def convertir_kilometros_a_millas(kilometros):
    # Fórmula: millas = kilómetros × 0.621371
    millas = kilometros * 0.621371
    return millas  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Convertir kilómetros a millas")
    
    # Pedimos los datos al usuario
    kilometros = float(input("Digita la cantidad en kilómetros: "))
    
    # Llamamos a la función convertir_kilometros_a_millas
    millas = convertir_kilometros_a_millas(kilometros)
    
    # Mostramos el resultado
    print(f"{kilometros} kilómetros equivalen a {millas} millas")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
