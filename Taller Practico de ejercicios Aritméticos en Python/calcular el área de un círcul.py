import math  # ✅ 1. Importamos la librería para usar pi


# 🔹 2. Definimos la función para calcular el área de un círculo
def calcular_area_circulo(radio):
    # Fórmula: A = π × r²
    area = math.pi * (radio ** 2)
    return area  # Retornamos el resultado


# 🔹 3. Definimos la función principal
def programa():
    print("Calcular el área de un círculo")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio del círculo: "))
    
    # Llamamos a la función calcular_area_circulo
    area = calcular_area_circulo(radio)
    
    # Mostramos el resultado
    print(f"El área del círculo es: {area}")


# 🔹 4. Llamamos la función principal para ejecutar el programa
programa()
