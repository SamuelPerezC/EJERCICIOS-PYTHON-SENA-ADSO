# 🔹 1. Definimos la función que verifica si el número es par o impar
def verificar_numero(numero):
    if numero % 2 == 0:
        print("El número es par.")
        return True     # Devuelve True si es par
    else:
        print("El número es impar.")
        return False    # Devuelve False si es impar


# 🔹 2. Definimos la función principal que maneja el bucle
def programa():
    # Solicitamos el primer número
    numero = int(input("Digite un número para iniciar el programa: "))

    # 🔁 Bucle que se ejecuta mientras el número sea par
    while verificar_numero(numero):      # Llama a la función verificar_numero
        numero = int(input("Digite otro número: "))

    # Cuando el número sea impar, termina el bucle
    print("Programa finalizado porque el número es impar.")


# 🔹 3. Llamamos a la función principal para iniciar el programa
programa()
