# Ejercicio 6: Calculadora simple
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese el número de la operación: ")

if opcion == '1':
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división es: {resultado}")
    else:
        print("Error: división por cero.")
else:
    print("Opción inválida.")
