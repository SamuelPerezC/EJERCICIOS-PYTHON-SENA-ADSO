# ✅ 1. No necesitamos librerías externas para este cálculo


# 🔹 2. Definimos la función para convertir Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit(celsius):
    # Fórmula: F = (C × 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit  # Retornamos el resultado


# 🔹 3. Definimos la función principal
def programa():
    print("Convertir grados Celsius a grados Fahrenheit")
    
    # Pedimos los datos al usuario
    celsius = float(input("Digita la temperatura en grados Celsius: "))
    
    # Llamamos a la función convertir_celsius_a_fahrenheit
    fahrenheit = convertir_celsius_a_fahrenheit(celsius)
    
    # Mostramos el resultado
    print(f"{celsius} °C equivalen a {fahrenheit} °F")


# 🔹 4. Llamamos la función principal para ejecutar el programa
programa()
