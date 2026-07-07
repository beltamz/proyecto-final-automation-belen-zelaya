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

@pytest.fixture
def inventory_page_obj(login_in_driver):
    return InventoryPage(login_in_driver)

@pytest.fixture
def cart_page_obj(login_in_driver):
    return CartPage(login_in_driver)

@pytest.hookimpl(tryfirst=True, hookwrapper= True)
def pytest_runtest_makereport(item, call):
    outcome= yield

    report= outcome.get_result()

    if report.when == "call" and report.failed:
        driver= item.funcargs.get("driver")

        if driver:
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents= True, exist_ok=True)

            file_name= target / f"{item.name}.png"

            driver.save_screenshot(str(file_name))

            #if hasattr(report, "extra"):
            #    report.extra.append({
            #        "name": "screenshot",
            #        "format": "image",
            #        "content": str(file_name)
            #    })

            extras= getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(str(file_name)))

            report.extras = extras