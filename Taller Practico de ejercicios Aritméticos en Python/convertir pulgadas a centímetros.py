# 🔹 1. Definimos la función para convertir pulgadas a centímetros
def convertir_pulgadas_a_centimetros(pulgadas):
    # Fórmula: centímetros = pulgadas × 2.54
    centimetros = pulgadas * 2.54
    return centimetros  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Convertir pulgadas a centímetros")
    
    # Pedimos los datos al usuario
    pulgadas = float(input("Digita la cantidad en pulgadas: "))
    
    # Llamamos a la función convertir_pulgadas_a_centimetros
    centimetros = convertir_pulgadas_a_centimetros(pulgadas)
    
    # Mostramos el resultado
    print(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
