from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def titulo_inventario(login_in_driver):
    driver= login_in_driver
    tituloProducto= driver.find_element(By.CSS_SELECTOR, ".header_secondary_container span")
    return tituloProducto.text


def productos_mostrados(login_in_driver):
    driver=login_in_driver
    try:
        productosListados= driver.find_elements(By.CLASS_NAME, "inventory_item")
        return len(productosListados)
    except Exception as e:
        print(f"Error en productos_mostrados: {e}")


def nombre_producto_especifico(login_in_driver):
    driver=login_in_driver
    nombreProductoEspecifico= driver.find_element(By.CSS_SELECTOR,"#item_4_title_link div")
    return nombreProductoEspecifico.text


def precio_producto_especifico(login_in_driver):
    driver=login_in_driver
    precioProducto= driver.find_element(By.CSS_SELECTOR,".pricebar div")
    return precioProducto.text

def mostrar_menu(login_in_driver):
    driver=login_in_driver
    menuBtn= driver.find_element(By.ID, "react-burger-menu-btn")
    menuBtn.click()
    #Configuro la espera (10 seg)
    wait=WebDriverWait(driver,10)
    #Una vez que hace click, espera hasta que vea el menu abierto (max 10 seg)
    menuMostrado = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))

    return menuMostrado.is_displayed()


def filtro_esta(login_in_driver):
    driver= login_in_driver
    filtro=driver.find_element(By.CLASS_NAME, "product_sort_container")
    return filtro.is_displayed()

def agregar_mochila_al_carrito(login_in_driver):
    driver= login_in_driver
    btnAgregarCarrito=driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    btnAgregarCarrito.click()
    try:
        btnRemove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        return btnRemove.is_displayed()
    except:
        return False
    
def ver_numero_en_carrito(product_added_in_driver):
    driver= product_added_in_driver
    wait=WebDriverWait(driver,10)
    cantEnCarrito= wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='shopping-cart-badge']" )))

    return cantEnCarrito.text


def ir_a_pagina_del_carrito(product_added_in_driver):
    driver= product_added_in_driver
    btnCarrito= driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    btnCarrito.click()
    return driver
