import pytest
from page.checkout_page import CheckoutPage
from utils.data_reader import read_checkout_csv

@pytest.mark.parametrize("customer", read_checkout_csv())
def test_successful_checkout(inventory_page_obj, cart_page_obj, driver, customer):
    #Agregamos un producto y entramos al carrito
    inventory_page_obj.agregar_producto_por_nombre(customer["producto"]) 
    inventory_page_obj.ir_al_carrito()
    
    #En el carrito, hacemos clic en ir a Checkout
    cart_page_obj.ir_a_checkout()
    
    #Inicializamos CheckoutPage para manejar el pago
    checkout_page = CheckoutPage(driver)
    
    #Completamos el step one con los datos de csv
    checkout_page.completar_datos_envio(
        customer["nombre"], 
        customer["apellido"], 
        customer["codigo_postal"]
    )
    
    #Completamos el step 2 y obtenemos el resultado
    texto_confirmacion = checkout_page.finalizar_compra()
    
    #Validamos que la compra fue exitosa
    assert texto_confirmacion == "Thank you for your order!", "El checkout no se completo correctamente"