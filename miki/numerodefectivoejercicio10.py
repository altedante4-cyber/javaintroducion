def numeroabundante(digito):

    acomulador = 0
    for i in range(1,digito):

        if digito % i == 0:
            acomulador += i


    if acomulador < digito:
        return True
    return False


def mostrarabundante(a,b):

    for i in range(a,b+1):

        if numeroabundante(i):
            print(i)




mostrarabundante(1,50)
