def codificar_mensaje(mensaje):
    lista_abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lista_abecedario2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z']

    #creamos la tupla a devolver

    lista_devolvcer = []


    for i in range(len(mensaje)):
        encontrado = False

        for j in range(len(lista_abecedario2)):

            if mensaje[i] == lista_abecedario2[j]:

                encontrado = True
                break
        if encontrado:
            lista_devolvcer.append(j + 1 )

    lista_tuple = tuple(lista_devolvcer,)

    #aprendi que se puede poner el reveersed en listas
    #aprendi a utilizar la funcion sum en tulas

    t = (mensaje , list(reversed(lista_tuple)) , sum(lista_tuple))

    return t

print(codificar_mensaje("hola"))