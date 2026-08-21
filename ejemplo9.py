nota1 = float(input("Ingrese un numero: "))
nota2 = float(input("Ingrese un numero: "))
nota3 = float(input("Ingrese un numero: "))
nota4 = float(input("Ingrese un numero: "))
nota5 = float(input("Ingrese un numero: "))

promedio = (nota1*0.30) + (nota2*0.15) + (nota3*0.15) + (nota4*0.20) + (nota5*0.20)

if promedio>=3:
    print("APROBADO")
    print(f"El promedio de las cinco notas fue: {promedio}")

