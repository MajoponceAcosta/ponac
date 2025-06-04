# Ejercicio 7: Edad en años, meses y días
edad_anios = int(input("Ingrese su edad en años: "))

meses = edad_anios * 12
dias = edad_anios * 365  # Aproximadamente, ignorando años bisiestos

print(f"Tienes aproximadamente {meses} meses o {dias} días de vida.")
