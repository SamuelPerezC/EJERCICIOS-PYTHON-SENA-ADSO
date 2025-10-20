# 1. CREAR CLASE
class Servidor:

    # 2. CONSTRUCTOR
    def __init__(self, nombre_servidor, estado):
        # 3. ATRIBUTOS
        self.nombre_servidor = nombre_servidor
        self.estado = estado

    # 4. MÉTODOS
    def muestra_pagina(self):
        if self.estado:
            return f"Mostrando página desde {self.nombre_servidor}"
        else:
            return "Servidor no disponible"

    def envia_sugerencia(self, sugerencia):
        if self.estado:
            return f"Sugerencia enviada: {sugerencia}"
        else:
            return "No se pudo enviar sugerencia. Servidor apagado."

    def envia_datos_de_compra(self, datos_compra):
        if self.estado:
            return f"Datos de compra enviados: {datos_compra}"
        else:
            return "No se pudo enviar datos de compra. Servidor apagado."

    def envia_datos_de_venta(self, datos_venta):
        if self.estado:
            return f"Datos de venta enviados: {datos_venta}"
        else:
            return "No se pudo enviar datos de venta. Servidor apagado."


# ---------------------------------------------------------
# 5. INSTANCIA DE OBJETO
obj_servidor = Servidor("ServidorPrincipal", True)

# 6. LLAMADO DE MÉTODOS
print(obj_servidor.muestra_pagina())
print(obj_servidor.envia_sugerencia("Agregar más productos deportivos"))
print(obj_servidor.envia_datos_de_compra({"producto": "Zapatos Jordan", "precio": 95000}))
print(obj_servidor.envia_datos_de_venta({"venta_id": 123, "total": 95000}))
