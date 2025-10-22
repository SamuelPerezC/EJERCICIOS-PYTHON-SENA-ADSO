# 🔹 1. Definimos la función para calcular el producto de dos números
def multiplicar_numeros(numero1, numero2):
    # Fórmula: producto = número1 * número2
    producto = numero1 * numero2
    return producto  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Producto de dos números")
    
    # Pedimos los datos al usuario
    numero1 = float(input("Digita el primer número: "))
    numero2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función para calcular el producto
    resultado = multiplicar_numeros(numero1, numero2)
    
    # Mostramos el resultado
    print(f"El producto de {numero1} y {numero2} es: {resultado}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
