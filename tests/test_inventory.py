from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.InventoryPage import titulo_inventario, productos_mostrados, nombre_producto_especifico

def test_inventory_title(login_in_driver):
    try:
        texto= titulo_inventario(login_in_driver)
        assert texto == "Products"
    except Exception as e:
        print(f"Error en el titulo del inventario: {e}")
        raise

def test_products_displayed(login_in_driver):
        containerEsta= productos_mostrados(login_in_driver)
        assert containerEsta == True

def test_specific_product_name(login_in_driver):
    try:
        nameProduct= nombre_producto_especifico(login_in_driver)
        assert nameProduct == "Sauce Labs Backpack"
    except Exception as e:
        print(f"Error en nombre_producto_especifico: {e}")
        raise