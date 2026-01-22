try:

    limite = int(input("introduce un nuermo "))

    if limite < 0 :

        print("numeros positivos")
    else:

        a = 0
        b = 1 

        sucesion = []

        while a <= limite:

            sucesion.append(str(a))

            siguiente = a + b
            a=b
            b = siguiente 

        print(','.join(sucesion))


except ValueError:
    print("error")

