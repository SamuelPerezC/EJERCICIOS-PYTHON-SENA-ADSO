# 🔹 1. Definimos la función para convertir litros a galones
def convertir_litros_a_galones(litros):
    # 1 galón = 3.78541 litros
    galones = litros / 3.78541
    return galones  # Retornamos el resultado


# 🔹 2. Definimos la función principal
def programa():
    print("Convertir litros a galones")
    
    # Pedimos los datos al usuario
    litros = float(input("Digita la cantidad de litros: "))
    
    # Llamamos a la función para hacer la conversión
    galones = convertir_litros_a_galones(litros)
    
    # Mostramos el resultado
    print(f"{litros} litros equivalen a {galones} galones")


# 🔹 3. Llamamos la función principal para ejecutar el programa
programa()
