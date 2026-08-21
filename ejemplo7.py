a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

# a es mayor
if a>b and a>c:
    if b > c:
        print(f"El orden descendente es: {a}, {b}, {c}")
    else:
        print(f"El orden descendente es: {a}, {c}, {b}")

# b es mayor
elif b > a and b > c:
    if a > c:
        print(f"El orden descendente es: {b}, {a}, {c}")
    else:
        print(f"El orden descendente es: {b}, {c}, {a}")

# c es mayor
else:
    if a>b:
        print(f"El orden descendente es: {c}, {a}, {b}")
    else:
        print(f"El orden descendente: {c}, {b}, {a}")
