num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

num1 = num1 + 3
num1 = num1 + 3
num1 = num1 + 3
num1 = num1 + 3

num2 = num2*3
num2 = num2*3
num2 = num2*3

nombre1 = input(f"Copie el nombre para el numero {num1}: ")
nombre2 = input(f"Copie el numero para el numero {num2}: ")

# con operador %
print("El numero %d se llama %s y el numero %d se llama %s" %(num1,nombre1,num2,nombre2))
print("El numero {} se llama {} y el  numero {} se llama {}".format(num1,nombre1,num2,nombre2))
print(f"El numero {num1} se llama {nombre1} y el numero {num2} se llama {nombre2}")
