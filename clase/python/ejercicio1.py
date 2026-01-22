

n = int(input("ingrese el numero "))


if n <= 0 :
    print("el numero deve ser prositivo")

else:
    factorial = 1


    i = 1

    while i <= n:

        factorial *= i

        

        i += 1 
    print(f"el factorial de {n} es {factorial}")



