# =======================================
#           CLASE SERVIDOR
# =======================================
class Servidor:
    def __init__(self):
        self.estado = "Activo"

    def muestra_pagina(self):
        print("Mostrando página web del servidor...")

    def envia_sugerencia(self, sugerencia):
        print(f"Sugerencia enviada al servidor: {sugerencia}")

    def envia_datos_de_compra(self, datos):
        print(f"Datos de compra enviados: {datos}")

    def envia_datos_de_venta(self, datos):
        print(f"Datos de venta enviados: {datos}")


# =======================================
#           CLASE PROCESADOR
# =======================================
class Procesador:
    def __init__(self):
        self.estado = "Listo"

    def mandar_datos_de_venta(self, datos):
        print(f"Enviando datos de venta: {datos}")

    def mandar_articulo_online(self, articulo):
        print(f"Mandando artículo online: {articulo}")

    def enviar_sugerencia_administrador(self, sugerencia):
        print(f"Sugerencia al administrador: {sugerencia}")

    def modificar_stock(self, producto, cantidad):
        print(f"Modificando stock de {producto} a {cantidad} unidades")

    def realizar_cobro(self, valor):
        print(f"Cobrando ${valor}")

    def realizar_pago(self, metodo):
        print(f"Pago realizado con {metodo}")

    def actualiza_catalogo(self, info):
        print(f"Actualizando catálogo con: {info}")

    def realiza_busqueda(self, termino):
        print(f"Realizando búsqueda: {termino}")


# =======================================
#           CLASE RECOLECTOR
# =======================================
class Recolector:
    def __init__(self):
        self.estado = "Recolectando datos"

    def envia_novedades(self, info):
        print(f"Enviando novedades: {info}")


# =======================================
#           CLASE INDEXADOR
# =======================================
class Indexador:
    def __init__(self):
        self.estado = "Indexando"

    def actualiza_almacen(self, producto, cantidad):
        print(f"Actualizando almacén: {producto} con cantidad {cantidad}")

    def envia_resultado_busqueda(self, resultado):
        print(f"Enviando resultado de búsqueda: {resultado}")


# =======================================
#           CLASE USUARIO
# =======================================
class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.password = "1234"

    def enviar_sugerencia(self, sugerencia):
        print(f"Sugerencia enviada: {sugerencia}")

    def leer(self):
        print(f"{self.nombre} está leyendo...")

    def comprar(self, producto):
        print(f"{self.nombre} compró: {producto}")

    def vender(self, producto):
        print(f"{self.nombre} vendió: {producto}")

    def login(self, usuario, password):
        print(f"Usuario {usuario} inició sesión con usuario: {usuario}")

    def realizar_reclamacion(self, reclamo):
        print(f"Reclamación realizada: {reclamo}")


# =======================================
#           CLASE PRODUCTO
# =======================================
class Producto:
    def __init__(self, precio, nombre, autor, editorial, año, preferencias):
        self.precio = precio
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.año = año
        self.preferencias = preferencias

    def vender(self):
        print(f"Vendiendo producto: {self.nombre}")

    def comprar(self):
        print(f"Comprando producto: {self.nombre}")

    def ver_catalogo(self):
        print(f"Mostrando catálogo de productos...")


# =======================================
#           CLASE HILO
# =======================================
class Hilo:
    def __init__(self):
        self.tema = None

    def busca_novedades(self, tema):
        self.tema = tema
        print(f"Buscando novedades sobre: {tema}")


# =======================================
#           CLASE EDITORIAL
# =======================================
class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self, articulo):
        print(f"La editorial {self.nombre} ha vendido el artículo: {articulo}")


# =======================================
#           CLASE LIBRO
# =======================================
class Libro:
    def __init__(self, genero):
        self.genero = genero

    def mostrar_genero(self):
        print(f"Género del libro: {self.genero}")


# =======================================
#           CLASE REVISTA
# =======================================
class Revista:
    def __init__(self, categoria):
        self.categoria = categoria

    def mostrar_categoria(self):
        print(f"Categoría de la revista: {self.categoria}")


# =======================================
#  CLASE ARTÍCULO DE SEGUNDA MANO
# =======================================
class ArticuloSegundaMano:
    def __init__(self, nombre, clasificacion, vendedor):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.vendedor = vendedor

    def mostrar_info(self):
        print(f"Artículo: {self.nombre} | Clasificación: {self.clasificacion} | Vendedor: {self.vendedor}")


# =======================================
#           CLASE NOVEDADES
# =======================================
class Novedades:
    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self, nueva):
        self.clasificacion = nueva
        print(f"Clasificación de '{self.tema}' cambiada a: {nueva}")


# =======================================
#           CLASE ARTÍCULO ONLINE
# =======================================
class ArticuloOnline:
    def __init__(self, tema):
        self.tema = tema

    def publicar(self):
        print(f"Publicando artículo online con tema: {self.tema}")


