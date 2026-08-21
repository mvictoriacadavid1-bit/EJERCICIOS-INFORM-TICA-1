n = int(input("Ingrese un numero: "))

suma = 0
contador = 1

while True:
    if contador > n:
        break

    if contador %2 != 0:
        suma = suma + contador
        
    contador = contador + 1

print(f"La suma de los numeros impares entre 1 y {n} es: {suma}")

