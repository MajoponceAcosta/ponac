# Ejercicio 5: Intercambiar valores entre dos variables sin usar una tercera variable
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

print(f"Antes del intercambio: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"Después del intercambio: a = {a}, b = {b}")
