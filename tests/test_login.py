def test_login_validation(login_in_driver):
    driver= login_in_driver
    #Verificamos que el inicio de sesion fue exitoso al redirigirnos a la pag de inventario
    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"