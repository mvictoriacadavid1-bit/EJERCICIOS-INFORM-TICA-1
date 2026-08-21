n = int(input("Ingrese un número (máx 9): "))
x = int(input("Ingrese un exponente (máx 9): "))

contador = 0

while True:
    if contador > n:
        break
    resultado = contador**x
    print(f"El contador {contador} elevado a la {x} es: {resultado}")
    contador = contador + 1


    