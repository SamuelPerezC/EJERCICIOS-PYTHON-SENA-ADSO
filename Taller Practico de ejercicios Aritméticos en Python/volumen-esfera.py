import math  # Importamos la librería para usar pi


# 🔹 1. Definimos la función para calcular el volumen
def calcular_volumen_esfera(radio):
    # Fórmula: V=34​πr3
    volumen = (4/3) * math.pi * (radio ** 3)
    return volumen   # Retornamos el resultado
# 🔹 2. Definimos la función principal
def programa():
    print("Cálcular el volumen de una esfera")
    
    # Pedimos los datos al usuario
    radio = float(input("Digita el radio de la esfera: "))
    
    
    # Llamamos a la función calcular_volumen_esfera
    volumen = calcular_volumen_esfera(radio)
    
    # Mostramos el resultado
    print(f"El volumen de la esfera es: {volumen}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()