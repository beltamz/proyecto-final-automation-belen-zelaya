import requests
from utils.logger import logger

headers= {
    "x-api-key": "pub_d57af02e0e6d0473015b0d9dfbe25c894e8015d3e2899540a19b8376201a22a2"
}

def test_login_valido():
    logger.info("Iniciando test de login valido (Desde la API ReqRes)...")

    body = {
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }

    logger.info("Enviando email y contraseña con POST...")
    response = requests.post("https://reqres.in/api/login", headers= headers, json= body)
    assert response.status_code==200
    logger.info("Logueo exitoso")


def test_login_sin_password():
    logger.info("Iniciando test de login no valido (sin contraseña)[Desde la API ReqRes]...")
    body = {
        "email":"eve.holt@reqres.in"
    }

    logger.info("Enviando solo el email con POST")
    response = requests.post("https://reqres.in/api/login", headers= headers, json= body)

    assert response.status_code == 400
    logger.info("Test de login no valido finalizado con exito")


def test_create_user():
    logger.info("Iniciando test para crear un usuario (Desde la API ReqRes)")

    body = {
        "name": "Tom",
        "email":"tom.swam@reqres.in",
        "password":"abc123*"
    }

    logger.info("Verificando que el email y la contraseña tengan el formato correcto...")
    assert body["email"].count("@") ==1
    assert "*" in body["password"]
    logger.info("Email y contraseña verificados correctamente")
   
    logger.info("Enviando los datos del usuario requeridos")
    response = requests.post("https://reqres.in/api/users", headers= headers, json= body)
    data = response.json()
    assert response.status_code==201
    logger.info("Datos recibidos correctamente")

    logger.info("Validando que los datos coincidan")
    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds()< 2
    logger.info("Tiempo de respuesta: menos de 2 segundos")


def test_delete_user():
    logger.info("Iniciando test para borrar un usuario (Desde la API ReqRes)")
    
    logger.info("Enviando DELETE para el usuario con id=2")
    response = requests.delete("https://reqres.in/api/users/2", headers= headers)
    
    assert response.status_code == 204
    logger.info("Usuario borrado con exito")


def test_get_user():
    logger.info("Iniciando test para obtener datos de un usuario (Desde la API ReqRes)")

    logger.info("Enviando GET para consultar el usuario con id=2")
    response = requests.get("https://reqres.in/api/users/2", headers= headers)

    assert response.status_code == 200
    logger.info("Usuario encontrado con exito")

    assert response.elapsed.total_seconds() < 2