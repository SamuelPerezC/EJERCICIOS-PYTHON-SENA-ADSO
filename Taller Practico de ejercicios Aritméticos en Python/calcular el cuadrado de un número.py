# 🔹 1. Definimos la función para calcular el cuadrado de un número
def calcular_cuadrado(numero):
    # Fórmula: cuadrado = número * número
    cuadrado = numero * numero
    return cuadrado  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Calcular el cuadrado de un número")
    
    # Pedimos el dato al usuario
    numero = float(input("Digita un número: "))
    
    # Llamamos a la función para calcular el cuadrado
    resultado = calcular_cuadrado(numero)
    
    # Mostramos el resultado
    print(f"El cuadrado de {numero} es: {resultado}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
