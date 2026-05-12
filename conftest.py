import pytest
from selenium import webdriver
from utils.LoginPage import login
from utils.InventoryPage import agregar_mochila_al_carrito, ir_a_pagina_del_carrito

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver

@pytest.fixture
def product_added_in_driver(login_in_driver):
    agregar_mochila_al_carrito(login_in_driver)
    return login_in_driver

@pytest.fixture
def cart_in_driver(product_added_in_driver):
    driver=product_added_in_driver
    ir_a_pagina_del_carrito(driver)
    return driver