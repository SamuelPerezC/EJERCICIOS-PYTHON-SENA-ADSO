# 🔹 1. Definimos la función para calcular la suma de dos números
def sumar_numeros(numero1, numero2):
    # Fórmula: suma = número1 + número2
    suma = numero1 + numero2
    return suma  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Suma de dos números")
    
    # Pedimos los datos al usuario
    numero1 = float(input("Digita el primer número: "))
    numero2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función para calcular la suma
    resultado = sumar_numeros(numero1, numero2)
    
    # Mostramos el resultado
    print(f"La suma de {numero1} y {numero2} es: {resultado}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
