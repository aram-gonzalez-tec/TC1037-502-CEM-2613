# Simular la tirada de dos dados
# Pedir al usuario que adivine dentro de las siguientes
# opciones:
# 1) La suma de los dados es menor a 7
# 2) La suma de los dados es igual a 7
# 3) La suma de los dados es mayor a 7
# Después de adivinar, mostrar el resultado de la suma
# al usuario e indicarle si adivinó o no
import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

suma_dados = dado1 + dado2

adivinar = int(input("""Bienvenido al juego
1) La suma de los dados es menor a 7
2) La suma de los dados es igual a 7
3) La suma de los dados es mayor a 7
Ingresa la opción que deseas: """))

print(f"""El primer dado salió: {dado1}
El segundo dado salió: {dado2}
La suma de los dados fue: {suma_dados}""")

if adivinar == 1 and suma_dados < 7 or \
   adivinar == 2 and suma_dados == 7 or \
   adivinar == 3 and suma_dados > 7:
    print("¡Le has atinado!")
else:
    print("No le atinaste, suerte para la próxima.")


