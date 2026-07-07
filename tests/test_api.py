import requests

headers= {
    "x-api-key": "pub_d57af02e0e6d0473015b0d9dfbe25c894e8015d3e2899540a19b8376201a22a2"
}

def test_login_valido():
    body = {
        "email":"eve.holt@reqres.in",
        "password":"cityslicka"
    }

    response = requests.post("https://reqres.in/api/login", headers= headers, json= body)
    assert response.status_code==200


def test_login_sin_password():
    body = {
        "email":"eve.holt@reqres.in"
    }

    response = requests.post("https://reqres.in/api/login", headers= headers, json= body)
    assert response.status_code == 400

def test_create_user():
    body = {
        "name": "Tom",
        "email":"tom.swam@reqres.in",
        "password":"abc123*"
    }

    response = requests.post("https://reqres.in/api/users", headers= headers, json= body)
    data = response.json()
    assert response.status_code==201

    assert body["email"].count("@") ==1
    assert "*" in body["password"]

    assert data["name"] == body["name"]
    assert data["email"] == body["email"]

    assert response.elapsed.total_seconds()< 2

def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers= headers)
    assert response.status_code == 204

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2", headers= headers)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2
