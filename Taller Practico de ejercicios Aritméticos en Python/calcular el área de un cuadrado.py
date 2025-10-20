# 🔹 1. Definimos la función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    # Fórmula: A = lado × lado
    area = lado * lado
    return area  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el área de un cuadrado")
    
    # Pedimos los datos al usuario
    lado = float(input("Digita la longitud del lado del cuadrado: "))
    
    # Llamamos a la función calcular_area_cuadrado
    area = calcular_area_cuadrado(lado)
    
    # Mostramos el resultado
    print(f"El área del cuadrado es: {area}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
