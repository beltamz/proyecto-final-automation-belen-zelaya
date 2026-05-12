from utils.InventoryPage import titulo_inventario, productos_mostrados, nombre_producto_especifico, precio_producto_especifico, mostrar_menu, filtro_esta, agregar_mochila_al_carrito, ver_numero_en_carrito, ir_a_pagina_del_carrito

#Prueba titulo en /inventory.html
def test_inventory_title(login_in_driver):
    texto= titulo_inventario(login_in_driver)
    assert texto == "Products", "No se muestran el titulo correcto"

#Prueba si muestra los productos
def test_products_displayed(login_in_driver):
    cantidad= productos_mostrados(login_in_driver)
    assert cantidad > 0, "No se muestran los productos"

#Prueba si el nombre de un producto es correcto
def test_specific_product_name(login_in_driver):
    nameProduct= nombre_producto_especifico(login_in_driver)
    assert nameProduct == "Sauce Labs Backpack", "Nombre producto no coincide"

#Prueba si el precio de un producto es correcto
def test_specific_product_price(login_in_driver):
    precio = precio_producto_especifico(login_in_driver)
    assert precio == "$29.99", "Precio producto no coincide"
    
#Prueba la visibilidad del menu
def test_menu_is_displayed(login_in_driver):
    menuVisible = mostrar_menu(login_in_driver)
    assert menuVisible == True, "El menu no se muestra"

#Prueba si el elemento Filtro existe
def test_filter_is_displayed(login_in_driver):
    filtro= filtro_esta(login_in_driver)
    assert filtro==True, "Elemento filtro no visible"

#Prueba el boton de agregar al carrito
def test_add_to_cart_btn_is_clickable(login_in_driver):
    btnCambio= agregar_mochila_al_carrito(login_in_driver)
    assert btnCambio == True, "Boton agregar al carrito no funciona"

#Prueba si aparece un numero n en el carrito
def test_see_number_in_cart(product_added_in_driver):
    numero= ver_numero_en_carrito(product_added_in_driver)
    assert numero=="1", "Numero en carrito no es correcto"

#Prueba si abre /cart.html
def test_go_to_cart_page(product_added_in_driver):
    driver=ir_a_pagina_del_carrito(product_added_in_driver)
    assert "/cart.html" in driver.current_url, "No se redirigio al carrito"
