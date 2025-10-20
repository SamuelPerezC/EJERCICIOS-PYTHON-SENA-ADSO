# ZONA DE CLASES

# 1. CREAR CLASES
class Sensor_Aceite:  # Clase para el sensor de aceite

    # 2. CREAR METODO CONSTRUCTOR
    def __init__(self, estado, dato):  # Constructor de la clase
        # 3. CREAR ATRIBUTOS
        self.estado_sensor = estado
        self.dato_sensor = dato

        # 6. LLAMADO DE METODO (se llama automáticamente al crear el objeto)
        self.imprimir_dato()

    # 4. CREAR METODOS NORMALES
    def imprimir_dato(self):  # Método que imprime los datos del sensor
        print(f"estado sensor: {self.estado_sensor} - dato: {self.dato_sensor}")


# --------------------------------------------------------

# 1. CREAR CLASES
class Sensor_Gasolina:  # Clase para el sensor de gasolina

    # 2. CREAR METODO CONSTRUCTOR
    def __init__(self):
        # 3. CREAR ATRIBUTOS
        self.sensor_gasolina = ""
        self.estado_sensor = ""

    # 4. CREAR MÉTODO NORMAL (para mostrar el objeto)
    def __str__(self):
        info = "Estado Sensor: " + str(self.estado_sensor) + "\n"
        return info

    # 4. CREAR MÉTODO NORMAL (para recibir datos)
    def verificar_sensor(self, gasolina, estado):
        if gasolina == True and estado == "Activo":
            return "Sensor Activo"  # 7. RETORNO
        else:
            return "Sensor No Activo"  # 7. RETORNO


# --------------------------------------------------------

# 1. CREAR CLASE
class Vehiculo:  # Clase para el vehículo

    # 2. CREAR METODO CONSTRUCTOR
    def __init__(self, dato_gasolina, dato_aceite, dato_agua):
        # 3. CREAR ATRIBUTOS
        self.estado_agua = dato_agua
        self.estado_gasolina = dato_gasolina
        self.estado_aceite = dato_aceite

    # 4. CREAR MÉTODO NORMAL
    def prender_motor(self):
        if self.estado_gasolina == True and self.estado_aceite == True and self.estado_agua:
            return True  # 7. RETORNO
        else:
            return False  # 7. RETORNO


# --------------------------------------------------------
# ZONA DE CÓDIGO PRINCIPAL

# 5. HACER INSTANCIA OBJETO
obj_sensor_aceite = Sensor_Aceite(True, "Sensor Activo")  # 6. LLAMADO DE MÉTODO

# 5. HACER INSTANCIA OBJETO
obj_sensor_gasolina = Sensor_Gasolina()

# 6. LLAMADO DE MÉTODO (enviamos datos como argumentos)
estado_sensor_gasolina = obj_sensor_gasolina.verificar_sensor(True, "Activo")  # 7. RETORNO
print(obj_sensor_gasolina)  # (uso del método __str__)

# 5. HACER INSTANCIA OBJETO (creamos los valores que necesita el vehículo)
dato_aceite = True
dato_agua = True
dato_gasolina = True

# 5. HACER INSTANCIA OBJETO
obj_vehiculo = Vehiculo(dato_gasolina, dato_aceite, dato_agua)

# 6. LLAMADO DE MÉTODO (no necesita argumentos)
if obj_vehiculo.prender_motor():  # 7. RETORNO (True o False)
    print("Motor encendido.")
else:
    print("No se puede encender el motor.")
