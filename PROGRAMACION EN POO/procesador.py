# 1. CREAR CLASE
class Procesador:

    # 2. CONSTRUCTOR
    def __init__(self, nombre, estado):
        # 3. ATRIBUTOS
        self.nombre = nombre
        self.estado = estado

    # 4. MÉTODOS
    def mandar_datos_de_venta(self, datos):
        if self.estado:
            return f"Datos de venta enviados: {datos}"
        else:
            return "Procesador inactivo. No se enviaron los datos de venta."

    def envia_articulo_online(self, articulo):
        if self.estado:
            return f"Producto Solicitado: {articulo}"
        else:
            return "No se pudo procesar tu pedido. Intentelo de nuevo."

    def envia_sugerencia(self, sugerencia):
        if self.estado:
            return f"Sugerencia enviada: {sugerencia}"
        else:
            return "No se pudo enviar sugerencia. Servidor apagado."

    def modificar_stock(self, producto, cantidad):
        if self.estado:
            return f"Stock de '{producto}' modificado. Nueva cantidad: {cantidad}"
        else:
            return "Procesador inactivo. No se pudo modificar stock."
        
    def realziar_cobro(self, producto, precio):
        if self.estado:
            return f"El costo de '{producto}' es de : {precio}"
        else:
            return "Error de proceso de Cobro. Intentalo de nuevo."


# ---------------------------------------------------------
# 5. INSTANCIA DE OBJETO
obj_procesador = Procesador("ProcesandoDatos", True)

# 6. LLAMADO DE MÉTODOS
print(obj_procesador.mandar_datos_de_venta({"producto": "Jordan", "precio": 95000}))
print(obj_procesador.envia_articulo_online({"producto": "Zapatos Jordan", "precio": 95000}))
print(obj_procesador.envia_sugerencia("Agregar más productos deportivos"))
print(obj_procesador.modificar_stock("Zapatos Jordan", 25))
print(obj_procesador.realziar_cobro("Zapatos Jordan", 95000))