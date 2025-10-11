# 1️⃣ Definir o declarar las variables y funciones

# Definimos la función para identificar el tipo de número
# 🔹 FUNCIÓN ← Se define una FUNCIÓN llamada identificar_numero
def identificar_numero(numero):
    # Comprobamos si el número es mayor que 0
    if numero > 0:
        print("El número es Positivo.")      # Muestra si el número es positivo
    # Comprobamos si el número es igual a 0
    elif numero == 0:
        print("El número es Neutro.")        # Muestra si el número es neutro
    # Si no cumple las anteriores, entonces es negativo
    else:
        print("El número es Negativo.")      # Muestra si el número es negativo


# 2️⃣ Llamar o crear las variables necesarias

# Pedimos al usuario que ingrese un número (variable de entrada)
# 🔹 VARIABLE  ← Se define una VARIABLE llamada numero
numero = int(input("Digite un número: "))    # Convierte el valor ingresado a entero


# 3️⃣ Llamar la función y mostrar el resultado

# Llamamos a la función y le enviamos el número ingresado por el usuario
# 🔹 LLAMADO DE LA FUNCIÓN ← Se llama la función y se le pasa la variable numero
identificar_numero(numero)

