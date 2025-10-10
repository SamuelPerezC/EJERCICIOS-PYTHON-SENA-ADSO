# ************ código principal con funciones ************

# ---------------------------------------------------------
# FUNCIÓN: mostrar_menu()
# OBJETIVO: mostrar las opciones disponibles al usuario
# ---------------------------------------------------------
def mostrar_menu():
    # No hay variables que definir ni asignar aquí,
    # solo se muestran mensajes en pantalla.

    # Procesar datos (mostrar el menú):
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")


# ---------------------------------------------------------
# FUNCIÓN: procesar_opcion(letra)
# OBJETIVO: analizar la letra ingresada y ejecutar la acción correspondiente
# ---------------------------------------------------------
def procesar_opcion(letra):
    # Definir variables:
    # letra → almacena la opción que el usuario digitó

    # Asignar variables:
    # Convertimos la letra a minúscula para evitar errores si el usuario usa mayúsculas
    letra = letra.lower()

    # Procesar los datos (evaluar la opción elegida)
    if letra == 'a':
        print("Has seleccionado Actualizar Sistema.\n")
    elif letra == 'e':
        print("Has seleccionado Eliminar Catálogo.\n")
    elif letra == 'c':
        print("Has seleccionado Crear Productos.\n")
    elif letra == 's':
        print("Finalizó con éxito.\n")
        return False  # Finaliza el ciclo si el usuario elige 'S'
    else:
        print("Opción no válida. Intente nuevamente.\n")

    # Si no se elige salir, el ciclo continúa
    return True


# ---------------------------------------------------------
# FUNCIÓN PRINCIPAL: main()
# OBJETIVO: controlar el flujo del programa (mostrar menú, pedir datos, procesarlos)
# ---------------------------------------------------------
def main():
    # Definir variables:
    # continuar → controlará si el ciclo debe seguir o detenerse
    # letra → guardará lo que el usuario digite

    while True:  # Inicia un ciclo que se repite hasta que el usuario decida salir
        # Procesar datos (mostrar el menú al usuario)
        mostrar_menu()

        # Asignar variables (leer lo que el usuario digita)
        letra = input("Digite una opción: ")

        # Procesar datos (enviar la opción a la función y recibir el resultado)
        continuar = procesar_opcion(letra)

        # Si continuar es False, se rompe el ciclo
        if not continuar:
            break  # Sale del bucle si el usuario elige 'S'

    # Procesar datos (mensaje final)
    print("EL DO-WHILE ha finalizado.\n")


# ---------------------------------------------------------
# LLAMADA A LA FUNCIÓN PRINCIPAL
# ---------------------------------------------------------
main()

