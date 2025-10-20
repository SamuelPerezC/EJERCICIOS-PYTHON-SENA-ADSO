import math  # ✅ 1. Importamos la librería para usar pi


# 🔹 2. Definimos la función para calcular el volumen de un cilindro
def calcular_volumen_cilindro(radio, altura):
    # Fórmula: V = π × r² × h
    volumen = math.pi * (radio ** 2) * altura
    return volumen  # Retornamos el resultado


# 🔹 3. Definimos la función principal
def programa():
    print("Calcular el volumen de un cilindro")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la base del cilindro: "))
    altura = float(input("Digita la altura del cilindro: "))
    
    # Llamamos a la función calcular_volumen_cilindro
    volumen = calcular_volumen_cilindro(radio, altura)
    
    # Mostramos el resultado
    print(f"El volumen del cilindro es: {volumen}")


# 🔹 4. Llamamos la función principal para ejecutar el programa
programa()
