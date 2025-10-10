
# Definimos la función para identificar el tipo de número
def identificar_numero(numero):
    if numero > 0:
        print("El número es Positivo.")
    elif numero == 0:
        print("El número es Neutro.")
    else:
        print("El número es Negativo.")



# Pedimos un número al usuario
numero = int(input("Digite un número: "))

# Llamamos a la función y le enviamos el número ingresado
identificar_numero(numero)
