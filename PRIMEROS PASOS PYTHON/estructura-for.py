# ************ código principal con funciones ************

# Función para solicitar la cantidad de números al usuario
def solicitar_cantidad():
    cantidad = int(input("Digite la cantidad de números que desea sumar: "))
    return cantidad


# Función para realizar la sumatoria de los números
def calcular_suma(cantidad):
    suma = 0
    for i in range(cantidad):
        print("Digite el número " + str(i + 1) + ": ")
        numero = int(input())
        suma = suma + numero
    return suma


# ************ código principal del programa ************
def main():
    cantidad = solicitar_cantidad()     # Llamamos la función que pide la cantidad
    total = calcular_suma(cantidad)     # Llamamos la función que calcula la suma
    print("La sumatoria total es: " + str(total))


# Llamamos la función principal
main()
