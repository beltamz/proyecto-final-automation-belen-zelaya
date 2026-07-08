import pytest
from page.inventory_page import InventoryPage
from utils.data_reader import read_products_json
from utils.logger import logger

#Prueba titulo en /inventory.html
def test_inventory_title(inventory_page_obj):
    logger.info("Iniciando test de verificacion del titulo del inventario... ")  
    
    texto= inventory_page_obj.obtener_titulo()
    logger.info(f"Validando titulo obtenido: '{texto}'")

    assert texto == "Products", "No se muestran el titulo correcto"
    logger.info("Titulo verificado correctamente ")  

#Prueba si muestra los productos
def test_products_displayed(inventory_page_obj):
    logger.info("Iniciando test de aparicion de productos...")  

    lista_productos= inventory_page_obj.obtener_productos()
    logger.info(f"Cantidad de productos detectados en pantalla: {len(lista_productos)}")

    assert len(lista_productos)> 0, "No se muestran los productos"
    logger.info("Aparicion de productos verificada correctamente")  

#Prueba si el nombre de un producto es correcto
def test_specific_product_name(inventory_page_obj):
    logger.info("Iniciando test de mostrar el nombre correcto de un producto...")  
    primer_producto_json = read_products_json()[0]
    lista_productos_web = inventory_page_obj.obtener_productos()
    nombre_web = lista_productos_web[0].find_element(*inventory_page_obj.nombres_productos).text

    logger.info(f"Comparando nombre web: '{nombre_web}' con nombre esperado en JSON: '{primer_producto_json['nombre']}'")
    assert nombre_web == primer_producto_json["nombre"], "Nombre del producto no coincide con el JSON"
    logger.info("Nombre producto verificado correctamente")  

#Prueba la visibilidad del menu
def test_menu_is_displayed(inventory_page_obj):
    logger.info("Iniciando test de visibilidad del menu...")  
    menuVisible = inventory_page_obj.menu_visible()
    assert menuVisible == True, "El menu no se muestra"
    logger.info("Visibilidad del menu verificada correctamente")  

#Prueba si el elemento Filtro existe
def test_filter_is_displayed(inventory_page_obj):
    logger.info("Iniciando test de aparicion del elemento filtro...")  
    filtro= inventory_page_obj.filtro_visible()
    assert filtro==True, "Elemento filtro no visible"
    logger.info("Visibilidad del filtro verificada correctamente")  

#Prueba el boton de agregar al carrito
def test_add_to_cart_btn_is_clickable(inventory_page_obj):
    logger.info("Iniciando test de agregar producto al carrito...")  

    primer_producto_json = read_products_json()[0]
    logger.info(f"Agregando '{primer_producto_json['nombre']}' al carrito")
    inventory_page_obj.agregar_producto_por_nombre(primer_producto_json["nombre"])

    assert inventory_page_obj.obtener_contador_carrito()=="1", "El contador del carrito no aumento"
    logger.info("Producto agregado al carrito correctamente")  

#Prueba si abre /cart.html
def test_go_to_cart_page(inventory_page_obj):
    logger.info("Iniciando test de redireccion al carrito...")  
    inventory_page_obj.ir_al_carrito()
    logger.info(f"Validando la url actual...")

    assert "/cart.html" in inventory_page_obj.driver.current_url, "No se redirigio al carrito"
    logger.info("Acceso al carrito exitoso")  


#Prueba el filtro para la busqueda del producto por precio de menor a mayor
def test_filter_price_low_to_high(inventory_page_obj):
    logger.info("Iniciando test de aplicar filtro: Price (Low to High)")  
    inventory_page_obj.aplicar_filtro_por_valor("lohi")

    #Llamamos a la lista con precios de mi InventoryPage.py
    precios_obtenidos = inventory_page_obj.obtener_precios_lista()
    
    #Copiamos la lista y la ordenamos de menor a mayor
    precios_ordenados_esperados = sorted(precios_obtenidos)
    
    logger.info("Validando la aplicacion del filtro...")
    #Validamos que la lista con precios que obtuvimos al aplicar el filtro este ordenado
    assert precios_obtenidos == precios_ordenados_esperados, "El filtro de menor a mayor precio no funciona"
    logger.info("Filtro aplicado exitosamente")  