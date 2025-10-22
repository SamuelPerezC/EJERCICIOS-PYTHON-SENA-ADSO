# 🔹 1. Definimos la función para calcular el volumen de un cubo
def calcular_volumen_cubo(lado):
    # Fórmula: V = lado³
    volumen = lado ** 3
    return volumen  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el volumen de un cubo")
    
    # Pedimos los datos al usuario
    lado = float(input("Digita la longitud del lado del cubo: "))
    
    # Llamamos a la función calcular_volumen_cubo
    volumen = calcular_volumen_cubo(lado)
    
    # Mostramos el resultado
    print(f"El volumen del cubo es: {volumen}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
