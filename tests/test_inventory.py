from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_inventory(login_in_driver):
    try:
        driver= login_in_driver

        
    except Exception as e:
        print(f"Error en test_inventory: {e}")