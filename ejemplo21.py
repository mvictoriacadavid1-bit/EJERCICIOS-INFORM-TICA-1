while True:
    n = int(input("Ingrese un número entre 0 y 20: "))

    if n < 0 or n > 20:
        print("¡ERROR! El número estar entre 0 y 20")
    elif n>0 and n<20:
        factorial = 1
        contador = 1

        while True:
            if contador > n:
                break

            factorial = factorial * contador
            contador = contador + 1

        print(f"El factorial de {n} es: {factorial}")

    opción = input("¿Desea hacer otro cálculo? (escribe 'S' para sí u otra letras para salir): ")
    if opción != 'S':
        print("¡Programa terminado!")
        break


