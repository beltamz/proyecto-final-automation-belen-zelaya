import pytest
from page.checkout_page import CheckoutPage
from utils.data_reader import read_checkout_csv
from utils.logger import logger

@pytest.mark.parametrize("customer", read_checkout_csv())
def test_successful_checkout(inventory_page_obj, cart_page_obj, driver, customer):
    logger.info("Iniciando test de checkout exitoso... ")  

    #Agregamos un producto y entramos al carrito
    logger.info("Agregando un producto y redireccionando al carrito")  
    inventory_page_obj.agregar_producto_por_nombre(customer["producto"]) 
    inventory_page_obj.ir_al_carrito()
    logger.info("Redireccionamiento al carrito exitoso")
    
    #En el carrito, hacemos clic en Checkout
    logger.info("Redireccionando al Checkout")  
    cart_page_obj.ir_a_checkout()
    
    #Inicializamos CheckoutPage para manejar el pago
    checkout_page = CheckoutPage(driver)
    
    #Completamos el step one con los datos del checkout_data.csv
    logger.info("Completando formulario con datos del cliente...")
    checkout_page.completar_datos_envio(
        customer["nombre"], 
        customer["apellido"], 
        customer["codigo_postal"]
    )
    
    #Completamos el step 2 y obtenemos el resultado
    logger.info("Confirmando los datos de la compra...")
    texto_confirmacion = checkout_page.finalizar_compra()
    
    #Validamos que la compra fue exitosa
    assert texto_confirmacion == "Thank you for your order!", "El checkout no se completo correctamente"
    logger.info("Checkout exitoso")