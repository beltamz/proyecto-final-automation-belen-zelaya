from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(driver):
    driver.get("https://www.saucedemo.com/")

    #Ingresamos el usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    #Ingresamos la contraseña
    contrasenia = driver.find_element(By.ID, "password")
    contrasenia.send_keys("secret_sauce")

    #Enviamos la informacion
    contrasenia.send_keys(Keys.RETURN)