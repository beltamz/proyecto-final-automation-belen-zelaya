from utils.CartPage import verificar_producto_agregado

def test_check_product_in_cart(cart_in_driver):
    nombre=verificar_producto_agregado(cart_in_driver)
    assert nombre== "Sauce Labs Backpack"