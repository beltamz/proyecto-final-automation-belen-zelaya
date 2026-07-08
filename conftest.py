import pytest
from utils.data_reader import read_user_csv
from selenium import webdriver
from page.loginPage import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import pathlib
import pytest_html

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login_page = LoginPage(driver)
    user= read_user_csv()[0]
    login_page.login(user["username"] , user["password"] )
    return driver

#Fixture para reutilizar InventoryPage sin tener que loguearse en c/ test
@pytest.fixture
def inventory_page_obj(login_in_driver):
    return InventoryPage(login_in_driver)

# Fixture para reutilizar CartPage compartiendo la sesion activa del driver
@pytest.fixture
def cart_page_obj(login_in_driver):
    return CartPage(login_in_driver)

# Hook interno de Pytest que intercepta el resultado de cada prueba al ejecutarse
@pytest.hookimpl(tryfirst=True, hookwrapper= True)
def pytest_runtest_makereport(item, call):
    outcome= yield

    report= outcome.get_result()

    # Si la prueba falla durante la fase de ejecución ("call"), toma una captura de pantalla
    if report.when == "call" and report.failed:
        driver= item.funcargs.get("driver")

        if driver:
            # Crea la carpeta para guardar las capturas si no existe
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents= True, exist_ok=True)

            # Define el nombre de la captura usando el nombre exacto del test que fallo
            file_name= target / f"{item.name}.png"

            driver.save_screenshot(str(file_name))

            # Adjunta la captura de pantalla directamente dentro del reporte HTML generado
            extras= getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(str(file_name)))
            report.extras = extras