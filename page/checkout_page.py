from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        
        #Localizadores del /checkout-step-one(Datos del cliente)
        self.input_nombre = (By.ID, "first-name")
        self.input_apellido = (By.ID, "last-name")
        self.input_postal = (By.ID, "postal-code")
        self.btn_continue = (By.ID, "continue")
        
        #Localizador del /checkout-step-two(Revision de la compra)
        self.btn_finish = (By.ID, "finish")
        
        #Localizador del /checkout-complete
        self.mensaje_exito = (By.CLASS_NAME, "complete-header")

    def completar_datos_envio(self, nombre, apellido, codigo_postal):
        """Llena el formulario en checkout-step-one y avanza"""
        self.driver.find_element(*self.input_nombre).send_keys(nombre)
        self.driver.find_element(*self.input_apellido).send_keys(apellido)
        self.driver.find_element(*self.input_postal).send_keys(codigo_postal)
        self.driver.find_element(*self.btn_continue).click()

    def finalizar_compra(self):
        """Hace clic en Finish en checkout-step-two y devuelve el texto de éxito"""
        self.driver.find_element(*self.btn_finish).click()
        return self.driver.find_element(*self.mensaje_exito).text