def validar_tarjeta(datos:tuple):

    datos_lista = list(datos)

    for i in range(len(datos_lista)):
        datos1 = datos_lista[0]
        datos2 = datos_lista[1]
        datos3 = datos_lista[2]
        datos4 = datos_lista[3]

    for i in datos1:
        #sacasmos la longitud
        if not i.isdigit():
            return False
        else:
            #comprobamos la longitud
            datos1_longitud = len(datos1)

            if  int(datos1_longitud) != 16:
                return False


    for j in str(datos2):
            if not j.isdigit():
                return False
            else:
                if int(datos2) < 0  or int(datos2) > 12:
                    return False


    for k in str(datos3):

        if not k.isdigit():
            return False
        else:

            if int(datos3) < 2024 or int(datos3) > 2030:
                return False

    for l in datos4:

        if not l.isdigit():
            return False
        else:
            # sacamos los digitos que tiene solo puede tener 3 digitos

            digitos_cvv = len(datos4)

            if int(digitos_cvv) != 3:
                return False

    return True











print(validar_tarjeta(("1234567812345678", 12, 2025, "123")))
