a = float(input("Ingrese un número: "))
n = int(input("Ingrese hasta que número cuenta el ciclo: "))

suma = 0.0
i = 1

while True:
    if i> n:
        break

    termino = (1/a)**i
    suma = suma + termino
    i += 1

print(f"El resultado de la sumatoria es: {suma}")

