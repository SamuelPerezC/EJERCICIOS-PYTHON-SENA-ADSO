import math  # Usamos math para manejar la raíz cuadrada


# 🔹 1. Definimos la función para calcular el área del hexágono regular
def calcular_area_hexagono(lado):
    # Fórmula: (3 * √3 * lado²) / 2
    area = (3 * math.sqrt(3) * lado ** 2) / 2
    return area  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el área de un hexágono regular")
    
    # Pedimos el dato al usuario
    lado = float(input("Digita la longitud de un lado: "))
    
    # Llamamos a la función para calcular el área
    area = calcular_area_hexagono(lado)
    
    # Mostramos el resultado
    print(f"El área del hexágono regular con lado {lado} es: {area}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
