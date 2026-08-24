print("hola mundo")

# Declaracion de variables
nombre = "Estudiante"
edad = 20

#Muestra de datos
print("Hola", nombre)
print("Tu edad es:", edad)

# Variables de lista 
acciones = ["registrar", "autenticar"]
print(acciones)

# Diccionario
persona = {
    "nombre": "Juan",
    "edad": 20
}

print(persona["nombre"])

# Ejemplo practico 
modulos = {
    "usuarios": ["registrar", "autenticar"],
    "viajes": ["solicitar", "asignar_conductor"],
    "pagos": ["calcular_tarifa", "registrar_pago"]
}

for nombre, acciones in modulos.items():
    print(f"Módulo {nombre}: {', '.join(acciones)}")




