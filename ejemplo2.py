total_notas = float(input("Ingresar cantidad de notas: "))

suma = 0
vueltas = 0

while True:
    if vueltas == total_notas:
        break
    nota = float(input("Ingrese la nota: "))
    suma = suma + nota
    vueltas = vueltas + 1

promedio = suma/total_notas

print(f"El promedio final es: {promedio}")


