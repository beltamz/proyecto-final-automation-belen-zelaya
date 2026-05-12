from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#Funcion para ver que titulo nos muestra la pag /inventory.html
def titulo_inventario(login_in_driver):
    driver= login_in_driver
    tituloProducto= driver.find_element(By.CSS_SELECTOR, ".header_secondary_container span")
    return tituloProducto.text #nos retorna su titulo en texto

#Funcion para ver si hay productos a la vista en /inventory.html
def productos_mostrados(login_in_driver):
    driver=login_in_driver
    productosListados= driver.find_elements(By.CLASS_NAME, "inventory_item")
    return len(productosListados)

#Funcion para ver el nombre especifico de un producto
def nombre_producto_especifico(login_in_driver):
    driver=login_in_driver
    nombreProductoEspecifico= driver.find_element(By.CSS_SELECTOR,"#item_4_title_link div")
    return nombreProductoEspecifico.text

#Funcion para ver el precio de un producto
def precio_producto_especifico(login_in_driver):
    driver=login_in_driver
    precioProducto= driver.find_element(By.CSS_SELECTOR,".pricebar div")
    return precioProducto.text

#Funcion para acceder al menu
def mostrar_menu(login_in_driver):
    driver=login_in_driver
    menuBtn= driver.find_element(By.ID, "react-burger-menu-btn")
    menuBtn.click()
    #Al tener que hacer click para acceder al menu, le doy un tiempo de espera
    #Configuro la espera (10 seg)
    wait=WebDriverWait(driver,10)
    #Una vez que hace click, espera hasta que vea el menu abierto (max 10 seg)
    menuMostrado = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))

    return menuMostrado.is_displayed()

#Funcion para ver la interfaz de filtro
def filtro_esta(login_in_driver):
    driver= login_in_driver
    filtro=driver.find_element(By.CLASS_NAME, "product_sort_container")
    return filtro.is_displayed()

#Funcion para agregar un producto (mochila) al carrito
def agregar_mochila_al_carrito(login_in_driver):
    driver= login_in_driver
    btnAgregarCarrito=driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    btnAgregarCarrito.click()
    try:
        #El nombre de "add to cart" cambia a "remove" si el boton funciona
        btnRemove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        return btnRemove.is_displayed()
    except NoSuchElementException:
        return False
    
#Funcion para ver el numero en el carrito
def ver_numero_en_carrito(product_added_in_driver):
    driver= product_added_in_driver
    wait=WebDriverWait(driver,10)
    cantEnCarrito= wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='shopping-cart-badge']" )))

    return cantEnCarrito.text

#Funcion para navegar a /cart.html
def ir_a_pagina_del_carrito(product_added_in_driver):
    driver= product_added_in_driver
    btnCarrito= driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    btnCarrito.click()
    return driver
