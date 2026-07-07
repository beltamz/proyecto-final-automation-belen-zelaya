from page.loginPage import LoginPage #importo la clase
from utils.data_reader import read_user_csv
import pytest
from utils.logger import logger

@pytest.mark.parametrize("user", read_user_csv())
def test_login(driver, user):
    login_page= LoginPage(driver) #creamos un objeto
    login_page.login(user["username"], user["password"])
    if user["valid"]== "true":
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
        
    else:
        error= login_page.get_error_message()
        assert "Epic sadface" in error
        #assert False
