def validar_seri(serie: str):

    #validar que tenga 3 letras,guion, 3 digitos
    #primero validamos que su longitud sea de 7 distinto a 7

    contador_letras = 0
    contador_guion = 0
    contador_digitos = 0

    #vocales no permitidas

    vocales_no_permitidas = ['A','E','I','O','U']
    for i in range(len(serie.upper())):

        if serie[i] in vocales_no_permitidas:
            return False
        if serie[i].isalpha():
            contador_letras += 1
        elif serie[i].isdigit():
            contador_digitos += 1
        elif serie[i] == '-':
            contador_guion += 1


    if contador_letras == 3 and contador_guion == 1 and contador_digitos == 3:
        return True
    else:
        return False





    # no pueden ser vocales




    # debe aceptar minusculas / mayusculas






print(validar_seri("BCS-123"))
print(validar_seri("ABE-456"))