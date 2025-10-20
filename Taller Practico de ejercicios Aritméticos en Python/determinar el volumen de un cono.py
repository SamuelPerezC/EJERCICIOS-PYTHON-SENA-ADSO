import math  # ✅ 1. Importamos la librería para usar pi


# 🔹 2. Definimos la función para calcular el volumen de un cono
def calcular_volumen_cono(radio, altura):
    # Fórmula: V = (1/3) × π × r² × h
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    return volumen  # Retornamos el resultado


# 🔹 3. Definimos la función principal
def programa():
    print("Calcular el volumen de un cono")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la base del cono: "))
    altura = float(input("Digita la altura del cono: "))
    
    # Llamamos a la función calcular_volumen_cono
    volumen = calcular_volumen_cono(radio, altura)
    
    # Mostramos el resultado
    print(f"El volumen del cono es: {volumen}")


# 🔹 4. Llamamos la función principal para ejecutar el programa
programa()
