def validaramigos(a,b):

    lista_a = []
    lista_b = []

    for i in range(1,a):

        if a % i == 0 :
            lista_a.append(i)

    for j in range(1,b):

        if b % j == 0 :
            lista_b.append(j)

    suma_a = sum(lista_a)
    suma_b = sum(lista_b)

    if suma_a == b and suma_b == a:
        return True
    return False



if validaramigos(1184,1210):
    print("son amigasos")
else:
    print("no son amigasos")






