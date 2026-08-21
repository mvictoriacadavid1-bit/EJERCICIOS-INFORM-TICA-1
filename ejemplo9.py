a = float(input("Ingrese un numero: "))
b = float(input("Ingrese un numero: "))
c = float(input("Ingrese un numero: "))
d = float(input("Ingrese un numero: "))

# mayor
if a>b and a>c and a>d:
    mayor = a
elif b>a and b>c and b>d:
    mayor = b
elif c>a and c>b and c>d:
    mayor = c
else:
    mayor = d

# menor
if a<b and a<c and a<d:
    menor = a
elif b<a and b<c and b<d:
    menor = b
elif c<a and c<b and c<d:
    menor = c
else:
    menor = d

suma = mayor + menor

print(f"La suma entre el mayor: {mayor} y el menor: {menor} es {suma}")
