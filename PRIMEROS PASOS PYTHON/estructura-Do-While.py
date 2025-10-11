# ************ código principal con funciones ************

# ---------------------------------------------------------
# FUNCIÓN: mostrar_menu()
# OBJETIVO: mostrar las opciones del menú al usuario
# ---------------------------------------------------------
def mostrar_menu():
    # No hay variables que definir ni asignar aquí.
    # Solo se procesan los datos mostrando las opciones disponibles.

    # Procesar los datos (mostrar texto en pantalla)
    print("Digite la letra 'A' para Actualizar Sistema")
    print("Digite la letra 'E' para Eliminar Catálogo")
    print("Digite la letra 'C' para Crear Productos")
    print("Digite la letra 'S' para salir del programa")


# ---------------------------------------------------------
# FUNCIÓN: procesar_opcion(letra)
# OBJETIVO: analizar la opción ingresada por el usuario
# ---------------------------------------------------------
def procesar_opcion(letra):
    # Definir variables:
    # letra → contendrá la opción escrita por el usuario.

    # Asignar variables:
    
    opcion = letra.lower()
    # a función .lower() en Python se usa para convertir un texto a minúsculas, el usuario puede escribir A, a, C, etc.

    # Procesar los datos (verificar la opción elegida)
    if opcion == 'a':
        print("Has seleccionado Actualizar Sistema.\n")
        #El \n que ves dentro de las comillas (por ejemplo "Hola\n") es algo que se llama un carácter de escape,y su función es hacer un salto de línea — o sea, bajar el texto a la siguiente línea.
    elif opcion == 'e':
        print("Has seleccionado Eliminar Catálogo.\n")
    elif opcion == 'c':
        print("Has seleccionado Crear Productos.\n")
    elif opcion == 's':
        print("Finalizó con éxito.\n")
        return False  # Esto hace que se termine el ciclo (salir del programa)
    else:
        print("Opción no válida. Intente nuevamente.\n")

    # Si la opción no es 's', el programa continúa ejecutándose
    return True


# ---------------------------------------------------------
# FUNCIÓN PRINCIPAL: main()
# OBJETIVO: controlar el flujo del programa con un ciclo repetitivo
# ---------------------------------------------------------
def main():
    # Definir variables:
    # letra → guardará lo que el usuario digite en cada repetición.
    # continuar → controlará si el ciclo debe seguir o terminar.

    while True:
        # Procesar datos (mostrar menú en pantalla)
        mostrar_menu()

        # Asignar variables (leer la opción del usuario)
        letra = input("Digite una opción: ")

        # Procesar datos (enviar la opción a la función y obtener respuesta)
        continuar = procesar_opcion(letra)

        # Procesar datos (decidir si se detiene el ciclo)
        if not continuar:
            break  # Sale del ciclo si el usuario elige 'S'

    # Procesar datos (mensaje final de cierre)
    print("EL DO-WHILE ha finalizado.\n")


# ---------------------------------------------------------
# LLAMADA A LA FUNCIÓN PRINCIPAL
# ---------------------------------------------------------
main()




