# ************ código principal con funciones ************

# Definimos una función para mostrar el menú
def mostrar_menu():
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")


# Definimos una función para procesar la opción ingresada
def procesar_opcion(letra):
    if letra.lower() == 'a':
        print("Has seleccionado Actualizar Sistema.\n")
    elif letra.lower() == 'e':
        print("Has seleccionado Eliminar Catálogo.\n")
    elif letra.lower() == 'c':
        print("Has seleccionado Crear Productos.\n")
    elif letra.lower() == 's':
        print("Finalizó con éxito.\n")
        return False  # Esto hace que se termine el ciclo
    else:
        print("Opción no válida. Intente nuevamente.\n")
    return True  # Esto mantiene el ciclo activo


# ************ código principal del programa ************
def main():
    while True:
        mostrar_menu()
        letra = input("Digite una opción: ")
        continuar = procesar_opcion(letra)
        if not continuar:
            break  # Sale del ciclo si el usuario elige 'S'

    print("EL DO-WHILE ha finalizado.\n")


# Llamamos a la función principal
main()
