# 🔹 1. Definimos la función para calcular el área de un trapecio
def calcular_area_trapecio(base_mayor, base_menor, altura):
    # Fórmula: A = ((B + b) × h) / 2
    area = ((base_mayor + base_menor) * altura) / 2
    return area  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el área de un trapecio")
    
    # Pedimos los datos al usuario
    base_mayor = float(input("Digita la longitud de la base mayor: "))
    base_menor = float(input("Digita la longitud de la base menor: "))
    altura = float(input("Digita la altura del trapecio: "))
    
    # Llamamos a la función calcular_area_trapecio
    area = calcular_area_trapecio(base_mayor, base_menor, altura)
    
    # Mostramos el resultado
    print(f"El área del trapecio es: {area}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
