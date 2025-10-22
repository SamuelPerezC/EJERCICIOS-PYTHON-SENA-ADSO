# 🔹 1. Definimos la función para calcular el área de un paralelogramo
def calcular_area_paralelogramo(base, altura):
    # Fórmula: A = base × altura
    area = base * altura
    return area  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el área de un paralelogramo")
    
    # Pedimos los datos al usuario
    base = float(input("Digita la longitud de la base: "))
    altura = float(input("Digita la altura del paralelogramo: "))
    
    # Llamamos a la función calcular_area_paralelogramo
    area = calcular_area_paralelogramo(base, altura)
    
    # Mostramos el resultado
    print(f"El área del paralelogramo es: {area}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
