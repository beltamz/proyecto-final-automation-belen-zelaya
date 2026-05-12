#Selectors - Proyecto Talento Tech

##🔐Login Page
-Input Usuario : #user-name (id del campo de texto para usuario)
-Input contraseña : #password (id del campo de texto para contraseña)
-Login button: #login-button (id del campo de entrada tipo submit)
-Mensaje de error: [data-test="error"] - .error-message-container h3 (Subtitulo con el mensaje de error)

##🛍️Inventory Page
-Link y nombre del producto especifico (mochila): [data-test="inventory-item-name"] - #item_4_title_link div ( para acceder al producto)
-Titulo Products: [data-test="title"] - .header_secondary_container span   (Encabezado de la seccion de productos)
-Contenedor inventario: #inventory_container (Div que contiene la lista de productos)
-Texto precio: [data-test="inventory-item-price"] - .pricebar div (Etiqueta que muestra el valor del producto)
-Boton agregar al carrito: #add-to-cart-sauce-labs-backpack ( id del boton de agregar al carrito)
-Boton menu: #react-burger-menu-btn  (Boton para abrir el menu lateral)
-Menu lateral: .bm-menu-wrap (Contenedor del menu desplegable)
-Acceso al carrito: [data-test="shopping-cart-link"] (Enlace al carrito de compras)
-Boton filtros: .product_sort_container (Menu desplegable para ordenar los productos)
-Cantidad carrito: [data-test="shopping-cart-badge"] (Indicador de cantidad sobre el icono del carrito)

##🛒Cart Page
-Producto en el carrito: [data-test="inventory-item-name"] (Nombre del producto dentro de la lista de compra)