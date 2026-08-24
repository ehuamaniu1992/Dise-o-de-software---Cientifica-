import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1")

print("Estado:", respuesta.status_code)

usuario = respuesta.json()

print("Nombre:", usuario["name"])
print("Correo:", usuario["email"])
print("Telefono:", usuario["phone"])

