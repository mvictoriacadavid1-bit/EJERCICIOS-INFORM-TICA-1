# ingresar datos
peso1 = float(input("Ingrese el peso de la primera esfera: "))
tamaño1 = float(input("Ingrese el tamaño de la primera esfera: "))
peso2 = float(input("Ingrese el peso de la segunda esfera: "))
tamaño2 = float(input("Ingrese el tamaño de la segunda esfera: "))
peso3 = float(input("Ingrese el peso de la tercera esfera: "))
tamaño3 = float(input("Ingrese el tamaño de la tercera esfera: "))

pi = 3.14159

# calcular radio
radio1 = tamaño1/2
radio2 = tamaño2/2
radio3 = tamaño3/2

# calcular volumen
volumen1 = ((4/3)*pi*(radio1)**3)
volumen2 = ((4/3)*pi*(radio2)**3)
volumen3 = ((4/3)*pi*(radio3)**3)

# calcular densidad
densidad1 = (peso1/volumen1)
densidad2 = (peso2/volumen2)
densidad3 = (peso3/volumen3)

# primera esfera mayor densidad
if densidad1>densidad2 and densidad1>densidad3:
    print("La primera esfera tiene mayor densidad")
# segunda esfera mayor densida
elif densidad2>densidad1 and densidad2>densidad3:
    print("La segunda esfera tiene mayor densidad")
# tercera esfera mayor densidad
else:
    print("La tercera esfera tiene mayor densidad")


