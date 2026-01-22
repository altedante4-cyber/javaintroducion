def recibirpin(a,b,c,d):


    lista = [str(a) , str(b) , str(c) , str(d) ]


    numero1 = int(lista[0])
    numero2 = int(lista[1])
    numero3 = int(lista[2])
    numero4 = int(lista[3])


    lista_enteros = [numero1, numero2, numero3, numero4]


    return lista_enteros



lista_enteross = recibirpin(0,0,4,0)


lista = [['x' for _ in range(10)] for _ in range(4)]


for i in range(len(lista)):

    for j in range(len(lista[i])):
        indi = 10 - lista_enteross[0]
        indi1 = 10 - lista_enteross[1]
        indi2 = 10 - lista_enteross[2]
        indi3 = 10 - lista_enteross[3]
        if i == 0  and j >= indi  :
             print("0",end="")

        elif i == 1 and j >= indi1 :
            print("O" , end="")
        elif i == 2 and j >= indi2 :
            print("O" , end="")
        elif i == 3 and j >= indi3 :
            print("O" , end="")

        else:
            print(lista[i][j],end="")
    print()


