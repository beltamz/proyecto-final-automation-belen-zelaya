from page.loginPage import LoginPage #importo la clase
from utils.data_reader import read_user_csv
import pytest
from utils.logger import logger

@pytest.mark.parametrize("user", read_user_csv())
def test_login(driver, user):
    logger.info(f"Iniciando test de login para usuario {user['username']}")
    login_page= LoginPage(driver) #creamos un objeto
    
    logger.info("Enviando el formulario de login...")
    login_page.login(user["username"], user["password"])

    logger.info("Iniciando sesion...")
    if user["valid"]== "true":
        logger.info("Validando redireccionamiento al inventario...")  
        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"  
        logger.info("Sesion iniciada correctamente")  
    else:
        error= login_page.get_error_message()
        assert "Epic sadface" in error
        logger.info("Error al iniciar sesion")
