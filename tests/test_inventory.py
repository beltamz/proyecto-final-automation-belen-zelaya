"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys"""
from utils.InventoryPage import titulo_inventario, productos_mostrados, nombre_producto_especifico, precio_producto_especifico, mostrar_menu, filtro_esta

def test_inventory_title(login_in_driver):
    try:
        texto= titulo_inventario(login_in_driver)
        assert texto == "Products"
    except Exception as e:
        print(f"Error en el titulo del inventario: {e}")
        raise

def test_products_displayed(login_in_driver):
        cantidad= productos_mostrados(login_in_driver)
        assert cantidad > 0

def test_specific_product_name(login_in_driver):
    try:
        nameProduct= nombre_producto_especifico(login_in_driver)
        assert nameProduct == "Sauce Labs Backpack"
    except Exception as e:
        print(f"Error en nombre_producto_especifico: {e}")
        raise

def test_specific_product_price(login_in_driver):
    try:
        precio = precio_producto_especifico(login_in_driver)
        assert precio == "$29.99"
    except Exception as e:
        print(f"Error en precio_producto_especifico: {e}")
        raise
    
def test_menu_is_displayed(login_in_driver):
    try:
        menuVisible = mostrar_menu(login_in_driver)
        assert menuVisible == True
    except Exception as e:
        print(f"Error en mostrar menu: {e}")
        raise

def test_filtro_esta(login_in_driver):
    try:
        filtro= filtro_esta(login_in_driver)
        assert filtro==True
    except Exception as e:
        print(f"Error en elegir filtro: {e}")
        raise