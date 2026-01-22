import random

lista = []
for i in range(100):
    numero = random.randint(1,50)
    lista.append(numero)


print(lista)

lista_no_repetidos = []
lista_repetidos = set() # lo utilizo para sacar el que mas se repite e ir comparando con la lista original

for i in lista:

    if i not in lista_no_repetidos:
        lista_no_repetidos.append(i)

    else:
        lista_repetidos.add(i)



lista_repetidos_lista = list(lista_repetidos)
lista_auxiliar = []

for i in lista_repetidos_lista:

    contador = lista.count(i)

    lista_auxiliar.append([i,contador])


mayor_numero = lista_auxiliar[0][0]

mayor_contador = lista_auxiliar[0][1]

for numero , contador in lista_auxiliar:

    if contador > mayor_contador:
        mayor_contador = contador
        mayor_numero = numero


#para sacar el max y el min

maximo = lista_no_repetidos[0]
minimo = lista_no_repetidos[0]

for i in range(len(lista_no_repetidos)):
    if lista_no_repetidos[i] > maximo:
        maximo = lista_no_repetidos[i]
    elif lista_no_repetidos[i] < minimo:
        minimo = lista_no_repetidos[i]


print(f"el numero mayor es {maximo}")
print(f"el numero menor es {minimo}")
print(f"el numero que mas se repite es {mayor_numero}")
print(f"mayor contador es {mayor_contador}")

#aprendi a meteer valores sobre  un array y dentro de ese oto array de dos vlaores y tambien
# a sacar de dichos array sus menor y maximo


