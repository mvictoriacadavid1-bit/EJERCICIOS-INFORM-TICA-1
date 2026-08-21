a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

resultado = 0 
vueltas = 0

while True:
    if vueltas == b:
        break
    resultado = resultado + a
    vueltas = vueltas + 1

print(f"El resultado es: {resultado}")

