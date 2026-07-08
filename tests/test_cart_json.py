import pytest
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from utils.data_reader import read_products_json
from utils.logger import logger

def test_cart_json(inventory_page_obj, cart_page_obj):
    logger.info("Iniciando test de carrito...")
    logger.info("Leyendo los productos guardados en JSON")
    productos= read_products_json()

    logger.info("Agregando productos del json al carrito...")
    for producto in productos:
        inventory_page_obj.agregar_producto_por_nombre(producto['nombre'])

    logger.info("Redireccionando al carrito...")
    inventory_page_obj.ir_al_carrito()

    productos_carrito = cart_page_obj.obtener_productos_carritos()

    logger.info("Verificando que se hayan agregado correctamente los productos...")
    for producto_json in productos:
        encontrado= False
        for producto_carrito in productos_carrito:
            if(producto_carrito['nombre']== producto_json['nombre'] and producto_carrito['precio']== producto_json['precio'] ):
                encontrado = True
                break
        assert encontrado, f"Product incorrecto o faltante:{producto_json['nombre']}"
    
    logger.info("Productos agregados correctamente al carrito")