nombres = input("Ingrese un nombres: ")
número_de_inscripción = float(input("Ingrese número de inscripción: "))
estrato = float(input("Ingrese el estrato: "))
patrimonio = float(input("Ingrese el patrimonio: "))

if patrimonio>2000000 and estrato>3:
    incremento = patrimonio*0.03
    pago_matrícula = 50000 + incremento
else:
    pago_matrícula = 50000

print(f"----------------------------------------------------------")
print(f"Número de la inscripción: {número_de_inscripción}")
print(f"Nombres: {nombres}")
print(f"Pago de matrícula: {pago_matrícula}")
print(f"----------------------------------------------------------")


