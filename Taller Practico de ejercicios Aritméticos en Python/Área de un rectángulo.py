# 🔹 1. Definimos la función para calcular el área de un rectángulo
def calcular_area_rectangulo(longitud, ancho):
    # Fórmula: A = longitud × ancho
    area = longitud * ancho
    return area  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el área de un rectángulo")
    
    # Pedimos los datos al usuario
    longitud = float(input("Digita la longitud del rectángulo: "))
    ancho = float(input("Digita el ancho del rectángulo: "))
    
    # Llamamos a la función calcular_area_rectangulo
    area = calcular_area_rectangulo(longitud, ancho)
    
    # Mostramos el resultado
    print(f"El área del rectángulo es: {area}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
