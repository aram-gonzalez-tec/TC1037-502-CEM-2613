# FizzBuzz
# Ingresar un entero positivo n
# Si n es divisible entre 3 imprimir Fizz
# Si n es divisible entre 5 imprimir Buzz
# Si n es divisible entre 3 y 5 imprimir FizzBuzz
# Si n no es divisible ni entre 3 ni entre 5 imprimir n
n = int(input("Ingresa el valor de n: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)