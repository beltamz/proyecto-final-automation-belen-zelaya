from selenium import webdriver
from selenium.webdriver.common.by import By

def verificar_producto_agregado(cart_in_driver):
    driver= cart_in_driver
    #Buscamos el producto añadido, y luego retornamos el texto que contiene
    nombreProducto=driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    return nombreProducto.text