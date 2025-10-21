from diagramaUMLcopy import Servidor
from diagramaUMLcopy import Procesador
from diagramaUMLcopy import Recolector
from diagramaUMLcopy import Indexador
from diagramaUMLcopy import Usuario
from diagramaUMLcopy import Producto
from diagramaUMLcopy import Hilo
from diagramaUMLcopy import Editorial
from diagramaUMLcopy import Libro
from diagramaUMLcopy import Revista
from diagramaUMLcopy import Novedades
from diagramaUMLcopy import ArticuloOnline



# =======================================
#           CÓDIGO PRINCIPAL
# =======================================

# 1. Servidor
servidor = Servidor()
servidor.muestra_pagina()
servidor.envia_sugerencia("Muy buena interfaz")
servidor.envia_datos_de_compra("Producto A")
servidor.envia_datos_de_venta("Producto A vendido")

print("-" * 50)

# 2. Procesador
procesador = Procesador()
procesador.mandar_datos_de_venta("Producto A")
procesador.mandar_articulo_online("Articulo Online 1")
procesador.enviar_sugerencia_administrador("Mejorar tiempos de respuesta")
procesador.modificar_stock("Producto A", 20)
procesador.realizar_cobro(95000)
procesador.realizar_pago("Tarjeta de crédito")
procesador.actualiza_catalogo("Nuevo catálogo 2025")
procesador.realiza_busqueda("Jordan Cadence")

print("-" * 50)


# 3. Recolector
recolector = Recolector()
recolector.envia_novedades("Nuevas zapatillas disponibles")

print("-" * 50)

# 4. Indexador
indexador = Indexador()
indexador.actualiza_almacen("Producto B", 30)
indexador.envia_resultado_busqueda("Resultados de prueba")

print("-" * 50)

# 5. Usuario
usuario = Usuario("Samuel", "Pérez", "C1234", "Calle 10")
usuario.login("Samuel", "1234")
usuario.enviar_sugerencia("Más variedad de tallas")
usuario.leer()
usuario.comprar("Jordan Cadence")
usuario.vender("Air Force 1")
usuario.realizar_reclamacion("Producto con defecto")

print("-" * 50)

# 6. Producto
producto = Producto(95000, "Jordan Cadence", "Nike", "Editorial A", "2025", "Sin preferencia")
producto.vender()
producto.comprar()
producto.ver_catalogo()

print("-" * 50)

# 7. Hilo
hilo = Hilo()
hilo.busca_novedades("Zapatillas deportivas")

print("-" * 50)

# 8. Editorial
editorial = Editorial("Editorial A", "Calle 45 #12", "3001234567")
editorial.vender("Catálogo deportivo")

print("-" * 50)

# 9. Libro
libro = Libro("Ficción")
libro.mostrar_genero()

# 10. Revista
revista = Revista("Moda")
revista.mostrar_categoria()

# 11. Artículo de segunda mano
articulo_segunda = ArticuloSegundaMano("Zapatillas Retro", "Running", "Samuel")
articulo_segunda.mostrar_info()

# 12. Novedades
novedades = Novedades("Zapatillas Retro", "Running")
novedades.cambiar_clasificacion("Urbano")

# 13. Artículo Online
articulo_online = ArticuloOnline("Nuevas Jordan 2025")
articulo_online.publicar()
