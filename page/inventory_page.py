from selenium.webdriver.common.by import By

class InventoryPage: 
    def __init__(self, driver):
        self.driver= driver

        #Locators
        self.titulo_inventario= (By.CSS_SELECTOR, ".header_secondary_container span")
        self.productos_mostrados = (By.CLASS_NAME, "inventory_item")
        self.mostrar_menu = (By.ID, "react-burger-menu-btn")
        self.filtro_esta = (By.CLASS_NAME, "product_sort_container")
        self.ver_numero_en_carrito = (By.CSS_SELECTOR,"[data-test='shopping-cart-badge']")
        self.ir_a_pagina_del_carrito = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.nombres_productos = (By.CLASS_NAME, "inventory_item_name")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")

    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo_inventario).text

    def obtener_productos(self):
        return self.driver.find_elements(*self.productos_mostrados)

    def menu_visible(self):
        return self.driver.find_element(*self.mostrar_menu).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self.filtro_esta).is_displayed()

    def obtener_contador_carrito(self):
        return self.driver.find_element(*self.ver_numero_en_carrito).text

    def ir_al_carrito(self):
        return self.driver.find_element(*self.ir_a_pagina_del_carrito).click()
    
    def agregar_producto_por_nombre(self, nombre_producto_json):
        productos= self.driver.find_elements(*self.productos_mostrados)
        
        for producto in productos: 
            nombre= producto.find_element(*self.nombres_productos).text
            if nombre == nombre_producto_json:
                producto.find_element(*self.add_to_cart_buttons).click()
                break