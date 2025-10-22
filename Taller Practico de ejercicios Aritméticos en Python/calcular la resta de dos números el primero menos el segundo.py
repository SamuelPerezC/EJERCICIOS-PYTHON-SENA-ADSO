# 🔹 1. Definimos la función para calcular la resta de dos números
def restar_numeros(numero1, numero2):
    # Fórmula: resta = número1 - número2
    resta = numero1 - numero2
    return resta  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Resta de dos números")
    
    # Pedimos los datos al usuario
    numero1 = float(input("Digita el primer número: "))
    numero2 = float(input("Digita el segundo número: "))
    
    # Llamamos a la función para calcular la resta
    resultado = restar_numeros(numero1, numero2)
    
    # Mostramos el resultado
    print(f"La resta de {numero1} menos {numero2} es: {resultado}")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
