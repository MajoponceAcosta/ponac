# Ejercicio 9: Verificar si un número es múltiplo de otro
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}.")
else:
    print(f"{num1} no es múltiplo de {num2}.")
