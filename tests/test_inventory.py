import pytest
from page.inventory_page import InventoryPage
from utils.data_reader import read_products_json

#Prueba titulo en /inventory.html
def test_inventory_title(inventory_page_obj):
    texto= inventory_page_obj.obtener_titulo()
    assert texto == "Products", "No se muestran el titulo correcto"

#Prueba si muestra los productos
def test_products_displayed(inventory_page_obj):
    lista_productos= inventory_page_obj.obtener_productos()
    assert len(lista_productos)> 0, "No se muestran los productos"

#Prueba si el nombre de un producto es correcto
def test_specific_product_name(inventory_page_obj):
    primer_producto_json = read_products_json()[0]
    lista_productos_web = inventory_page_obj.obtener_productos()
    nombre_web = lista_productos_web[0].find_element(*inventory_page_obj.nombres_productos).text
    assert nombre_web == primer_producto_json["nombre"], "Nombre del producto no coincide con el JSON"

#Prueba la visibilidad del menu
def test_menu_is_displayed(inventory_page_obj):
    menuVisible = inventory_page_obj.menu_visible()
    assert menuVisible == True, "El menu no se muestra"

#Prueba si el elemento Filtro existe
def test_filter_is_displayed(inventory_page_obj):
    filtro= inventory_page_obj.filtro_visible()
    assert filtro==True, "Elemento filtro no visible"

#Prueba el boton de agregar al carrito
def test_add_to_cart_btn_is_clickable(inventory_page_obj):
    primer_producto_json = read_products_json()[0]
    inventory_page_obj.agregar_producto_por_nombre(primer_producto_json["nombre"])
    assert inventory_page_obj.obtener_contador_carrito()=="1", "El contador del carrito no aumento"

#Prueba si abre /cart.html
def test_go_to_cart_page(inventory_page_obj):
    inventory_page_obj.ir_al_carrito()
    assert "/cart.html" in inventory_page_obj.driver.current_url, "No se redirigio al carrito"

#Prueba el filtro para la busqueda del producto por precio de menor a mayor
def test_filter_price_low_to_high(inventory_page_obj):
    inventory_page_obj.aplicar_filtro_por_valor("lohi")
    #Llamamos a la lista con precios
    precios_obtenidos = inventory_page_obj.obtener_precios_lista()
    #Copiamos la lista y la ordenamos de menor a mayor
    precios_ordenados_esperados = sorted(precios_obtenidos)
    
    #Validamos que la lista con precios que obtuvimos al aplicar el filtro este ordenado
    assert precios_obtenidos == precios_ordenados_esperados, "El filtro de menor a mayor precio no funciona"