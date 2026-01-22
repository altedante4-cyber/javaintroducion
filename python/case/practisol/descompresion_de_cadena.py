letra = input("introduce cadena")

i = 0 

while i < len(letra):

    numero = letra[i]
    caracter =letra[i +1]


    entero = int(numero)
    j = 0 


    while j < entero :

        print(caracter , end='')

        j += 1

    i += 2