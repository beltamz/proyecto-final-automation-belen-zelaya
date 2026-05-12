from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def verificar_producto_agregado(cart_in_driver):
    driver= cart_in_driver
    nombreProducto=driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    return nombreProducto.text