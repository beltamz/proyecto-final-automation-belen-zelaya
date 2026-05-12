#Selectors - Proyecto Talento Tech

##Login Page
-Input Usuario : #user-name (id del campo de texto para usuario)
-Input contraseña : #password (id del campo de texto para contraseña)
-Login button: #login-button (id del campo de entrada tipo submit)
-Mensaje de error: [data-test="error"] - .error-message-container h3 (Subtitulo con el mensaje de error)

##Inventory Page
-Link y nombre del producto especifico (mochila): [data-test="inventory-item-name"] - #item_4_title_link div ( para acceder al producto)
-Titulo Products: [data-test="title"] - .header_secondary_container span   (accedo al titulo products)
-Container inventario: #inventory_container
-Texto precio: [data-test="inventory-item-price"] - .pricebar div (accedo al precio)
-Boton agregar al carrito: #add-to-cart-sauce-labs-backpack ( id del boton de agregar al carrito)
-Boton para ver el menu: #react-burger-menu-btn
-Menu flotante: .bm-menu-wrap
-Acceder al carrito: [data-test="shopping-cart-link"]
-Boton para los filtros: .product_sort_container
-ver cant carrito: [data-test="shopping-cart-badge"]
(boton para volver al inventario (desde el carrito))
(boton para el checkout)
(si tenemos un producto en el carrito, boton para borrar)
-Ver producto en el carrito: [data-test="inventory-item-name"]


