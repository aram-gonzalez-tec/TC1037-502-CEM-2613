print(type(50)) # int -> integer -> número entero
print(type(14.3)) # float -> punto flotante -> número real
print(type(5j)) # complex -> número complejo
print(type("hola")) # str -> string -> texto
print(type('hola'))
print(type(True)) # bool -> booleano -> valores lógicos
print(type(False))
# tuple -> tupla
# Secuencia ordenada e inmutable de datos
print(type((2,5,2,True,"Hola")))
# list -> lista
# Secuencia ordenada y mutable de datos
print(type([2,5,2,True,"Hola"]))
# dict -> diccionario
# Secuencia ordenadas, nombradas y mutables de datos
print(type({"llave": ["cualquier", "cosa", 23]}))

alumno = {
    "nombre": "Pedro",
    "apellido paterno": "Martínez",
    "apellido materno": "Solís",
    "dirección": {
        "calle": "Calle",
        "número": 37
        }
    }

print(alumno)