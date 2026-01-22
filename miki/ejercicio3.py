def todecimal(cadena):
    lista = []

    #comprobar que realmente se esta recibiendo binario y no otros numero

    for i in cadena:

        if i != '1' and i != '0' :
            return -1
        else:
            lista.append(i)



    contador = 1

    lista_nueva = []

    for i in range(len(lista)):
            lista_nueva.append(contador)
            contador *= 2


    sumador = 0

    lista_alreves = lista_nueva[::-1]

    for i in range(len(lista)):

        if int(lista[i]) == 1 :
            sumador += lista_alreves[i]



    return sumador



print(todecimal("10110"))
print(todecimal("345"))
print(todecimal("hola"))

















