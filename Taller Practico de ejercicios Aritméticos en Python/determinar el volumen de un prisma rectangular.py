# 🔹 1. Definimos la función para calcular el volumen de un prisma rectangular
def calcular_volumen_prisma_rectangular(longitud, ancho, altura):
    # Fórmula: V = longitud × ancho × altura
    volumen = longitud * ancho * altura
    return volumen  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el volumen de un prisma rectangular")
    
    # Pedimos los datos al usuario
    longitud = float(input("Digita la longitud del prisma: "))
    ancho = float(input("Digita el ancho del prisma: "))
    altura = float(input("Digita la altura del prisma: "))
    
    # Llamamos a la función calcular_volumen_prisma_rectangular
    volumen = calcular_volumen_prisma_rectangular(longitud, ancho, altura)
    
    # Mostramos el resultado
    print(f"El volumen del prisma rectangular es: {volumen}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
