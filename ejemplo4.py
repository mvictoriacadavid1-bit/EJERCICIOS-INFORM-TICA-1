a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

if a > b and a > c:
    # a es el mayor
    if b > c:
        print(f"El orden descendente es: {a}, {b}, {c}")
    else:
        print(f"El orden descendente es: {a}, {c}, {b}")
elif b > a and b > c:
    # b es el mayor
    if a > c:
        print(f"El orden descendente es: {b}, {a}, {c}")
    else:
        print(f"El orden descendente es: {b}, {c}, {a}")
else:
    # c es el mayor
    if a>b:
        print(f"El orden descendente es: {c}, {a}, {b}")
    else:
        print(f"El orden descendente: {c}, {b}, {a}")

