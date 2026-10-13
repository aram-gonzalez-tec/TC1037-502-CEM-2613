uf1 = float(input("Ingresa calificación 1: "))
uf2 = float(input("Ingresa calificación 2: "))
uf3 = float(input("Ingresa calificación 3: "))
uf4 = float(input("Ingresa calificación 4: "))
uf5 = float(input("Ingresa calificación 5: "))
uf6 = float(input("Ingresa calificación 6: "))
promedio = (uf1 + uf2 + uf3 + uf4 + uf5 + uf6) / 6
# Formas antiguas - no usar para entregas
print("Tu promedio fue:", promedio)
print("Tu promedio fue: " + str(promedio))
print("Tu promedio fue: {0:,.2f}".format(promedio))
# f-string
print(f"Tu promedio fue: {promedio:,.2f}")

