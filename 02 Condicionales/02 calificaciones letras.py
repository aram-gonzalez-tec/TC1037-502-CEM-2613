# Usando sólo if y else resolver lo siguiente:
# Permite que tu usuario ingrese una calificación numérica
# De acuerdo a su calificación imprime el equivalente en
# una escala de letras.
# 90 o más -> A
# 80 o más y menos de 90 -> B
# 70 o más y menos de 80 -> C
# Menos de 70 -> F

calificación = float(input("Ingresa la calificación: "))
if calificacion >= 90:
    print("A")
else:
    if calificación >= 80:
        print("B")
    else:
        if calificación >= 70:
            print("C")
        else:
            print("F")
            
if calificación >= 90:
    print("A")
if calificación >= 80 and calificación < 90:
    print("B")
if calificación >= 70 and calificación < 80:
    print("C")
if calificación < 70:
    print("F")


if calificacion >= 90:
    print("A")
elif calificación >= 80:
    print("B")
elif calificación >= 70:
    print("C")
else:
    print("F")
    
    
    
    
