from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#! Todo esto lo hice yo, chequear que funcione

def titulo_inventario(login_in_driver):
    driver= login_in_driver
    tituloProducto= driver.find_element(By.CSS_SELECTOR, ".header_secondary_container span")
    return tituloProducto.text


def productos_mostrados(login_in_driver):
    driver=login_in_driver
    try:
        contenedorProductos= driver.find_element(By.ID, "inventory_container")
        return contenedorProductos.is_displayed()
    except Exception as e:
        print(f"Error en productos_mostrados: {e}")


def nombre_producto_especifico(login_in_driver):
    driver=login_in_driver
    nombreProductoEspecifico= driver.find_element(By.CSS_SELECTOR,"#item_4_title_link div")
    return nombreProductoEspecifico.text

"""
def precio_producto_especifico(login_in_driver):
    driver=login_in_driver

"""
