from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys ##le agregue esta


class LoginPage:
    def __init__(self,driver):
        self.driver = driver #guardo el navegador en la clase

        #selectores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password") 
        self.error_password = (By.CSS_SELECTOR, "[data-test= 'error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)

    def ingresar_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def presionar_enter(self):
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER) 

    def login(self, usuario, password):
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.presionar_enter()

    def get_error_message(self):
        return self.driver.find_element(*self.error_password).text