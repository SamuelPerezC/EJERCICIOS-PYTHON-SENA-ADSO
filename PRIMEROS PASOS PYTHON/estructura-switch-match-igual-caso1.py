# ************ código principal con funciones ************

# Función que pide el número del mes
def pedir_numero():
    num = int(input("Digite un número del 1 al 12: "))
    return num


# Función que muestra el nombre del mes usando match-case
def mostrar_mes(num):
    match num:
        case 1:
            print("Enero")
        case 2:
            print("Febrero")
        case 3:
            print("Marzo")
        case 4:
            print("Abril")
        case 5:
            print("Mayo")
        case 6:
            print("Junio")
        case 7:
            print("Julio")
        case 8:
            print("Agosto")
        case 9:
            print("Septiembre")
        case 10:
            print("Octubre")
        case 11:
            print("Noviembre")
        case 12:
            print("Diciembre")
        case _:
            print("Número inválido. Debe ser entre 1 y 12.")


# ************ código principal del programa ************
def main():
    numero_mes = pedir_numero()  # Llamamos la función para pedir el número
    mostrar_mes(numero_mes)      # Mostramos el nombre del mes correspondiente


# Llamamos la función principal
main()
