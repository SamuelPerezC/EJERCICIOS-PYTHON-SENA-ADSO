# 🔹 1. Definimos la función que calcula el área
def calcular_area_triangulo(base, altura):
    # Fórmula: (base * altura) / 2
    area = (base * altura) / 2
    return area   # Retornamos el resultado
# 🔹 2. Definimos la función principal
def programa():
    print("Cálculo del área de un triángulo")
    
    # Pedimos los datos al usuario
    base = float(input("Digite la base del triángulo: "))
    altura = float(input("Digite la altura del triángulo: "))
    
    # Llamamos a la función calcular_area_triangulo
    area = calcular_area_triangulo(base, altura)
    
    # Mostramos el resultado
    print(f"El área del triángulo es: {area}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()