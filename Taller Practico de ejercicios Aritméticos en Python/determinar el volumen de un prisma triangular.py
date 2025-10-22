# 🔹 1. Definimos la función para calcular el volumen del prisma triangular
def calcular_volumen_prisma_triangular(base, altura, ancho):
    # Fórmula: Volumen = (1/2 * base * altura) * ancho
    volumen = (0.5 * base * altura) * ancho
    return volumen  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Determinar el volumen de un prisma triangular")
    
    # Pedimos los datos al usuario
    base = float(input("Digita la longitud de la base: "))
    altura = float(input("Digita la altura del triángulo: "))
    ancho = float(input("Digita el ancho del prisma: "))
    
    # Llamamos a la función para calcular el volumen
    volumen = calcular_volumen_prisma_triangular(base, altura, ancho)
    
    # Mostramos el resultado
    print(f"El volumen del prisma triangular es: {volumen}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
