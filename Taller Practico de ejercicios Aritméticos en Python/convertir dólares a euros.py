# 🔹 1. Definimos la función para convertir dólares a euros
def convertir_dolares_a_euros(dolares, tasa_cambio):
    # Fórmula: euros = dólares × tasa_cambio
    euros = dolares * tasa_cambio
    return euros  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Convertir dólares a euros")
    
    # Pedimos los datos al usuario
    dolares = float(input("Digita la cantidad en dólares: "))
    tasa_cambio = float(input("Digita la tasa de cambio (1 dólar = ? euros): "))
    
    # Llamamos a la función convertir_dolares_a_euros
    euros = convertir_dolares_a_euros(dolares, tasa_cambio)
    
    # Mostramos el resultado
    print(f"{dolares} dólares equivalen a {euros} euros")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
