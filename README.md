# Proyecto de Automatización de Pruebas QA - SauceDemo & ReqRes API
Por Belén Zelaya

## 📝Propósito del Proyecto
Este proyecto final consiste en el diseño y desarrollo de un framework de automatización de pruebas funcionales y de rendimiento de extremo a extremo (E2E). Se enfoca en validar los flujos críticos de la plataforma web [SauceDemo](https://www.saucedemo.com/) (interfaz de usuario) y la consistencia de los servicios backend simulados en [ReqRes API](https://reqres.in/). 

El framework está construido bajo una arquitectura escalable y profesional, implementando el patrón de diseño **Page Object Model (POM)**, pruebas guiadas por datos (**Data-Driven Testing**) y un sistema integral de trazabilidad mediante **Loggers**.

## 🛠️Tecnologías Utilizadas
- **Lenguaje:** Python 3.14+
- **Automatización UI:** Selenium WebDriver
- **Pruebas de API:** Requests
- **Framework de Testing:** Pytest
- **Reportes Avanzados:** Pytest-HTML
- **Gestión de Datos:** Archivos CSV y JSON

---

## 📁Estructura del Proyecto
La arquitectura del repositorio está organizada de forma modular para separar las responsabilidades de las pruebas, los localizadores de páginas y los datos de entrada:

├── proyecto-final-automation-belen-zelaya/
│   ├── data/
│   │   ├── checkout_data.csv       # Datos dinámicos para el formulario de pago
│   │   ├── productos.json          # Listado de productos esperados para validación cruzada
│   │   └── users.csv               # Credenciales para escenarios de login positivos y negativos
│   ├── page/                       # Clases del Patrón Page Object Model (POM)
│   │   ├── cart_page.py            # Localizadores y acciones del carrito de compras
│   │   ├── checkout_page.py        # Control del flujo de pago (Step One, Two y Complete)
│   │   ├── inventory_page.py       # Interacción con el catálogo y filtros de productos
│   │   └── loginPage.py            # Control de acceso y captura de mensajes de error
│   ├── tests/                      # Casos de prueba automatizados
│   │   ├── test_cart_json.py       # Validación de persistencia carrito vs JSON
│   │   ├── test_checkout.py        # Flujo del checkout con datos dinámicos
│   │   ├── test_inventory.py       # Pruebas de catálogo, menú, botones y ordenamiento por precio
│   │   ├── test_login_csv.py       # Escenarios parametrizados de login (válidos e inválidos)
│   │   └── test_api.py             # Pruebas funcionales de API (GET, POST, DELETE, Latencia)
│   ├── utils/                      # Módulos de soporte y utilidades
│   │   ├── data_reader.py          # Lectores automatizados de archivos CSV y JSON
│   │   └── logger.py               # Configuración central del sistema de logs
│   ├── pytest.ini                  # Configuración global del framework de testing

## 🚀Instalación y Requisitos
1. **Clonar el repositorio:**

   git clone [https://github.com/beltamz/pre-entrega-automation-testing--belen-zelaya-](https://github.com/beltamz/pre-entrega-automation-testing--belen-zelaya-)

2. **Navegar a la carpeta del proyecto:**

        cd proyecto-final-automation-belen-zelaya
    
3. **Instalar las dependencias externas:**
    Ejecutar el siguiente comando en tu terminal para instalar las librerías externas necesarias:

        pip install selenium webdriver-manager pytest pytest-html requests pathlib logging

## 🧪Ejecución de las Pruebas
Para ejecutar la suite completa de pruebas (UI y API) y generar el reporte automatizado:

    py -m pytest -v --html=report.html --self-contained-html

Si se desea ejecutar un archivo de prueba específico (ejemplo, solo API):

    py -m pytest -v tests/test_api.py

## 📊¿Cómo interpretar los reportes generados?
Al finalizar la ejecución, se generará un archivo interactivo llamado report.html en la raíz del proyecto. Para interpretarlo:

### Estado del Test (Result):
-PASSED (Verde): El flujo se completó con éxito y las validaciones (assert) se cumplieron al 100%.

-FAILED (Rojo): La prueba falló. Al desplegar el test, se mostrará el Traceback detallado indicando exactamente qué falló y en qué línea del código.

### Capturas de Pantalla Automatizadas (Screenshots):
Si un caso de prueba de la interfaz web (UI) falla, el framework (conftest.py) tomará una captura de pantalla del navegador de manera automática en el instante preciso del error y la adjuntará directamente dentro del reporte HTML para agilizar el diagnóstico.

### Trazabilidad por Consola (Logs):
Cada prueba escribe una bitácora detallada de sus acciones (ej. "Iniciando test...", "Validando orden de precios"). En caso de fallo, los logs te permitirán conocer cuál fue el último paso exitoso antes de encontrarse con el inconveniente.