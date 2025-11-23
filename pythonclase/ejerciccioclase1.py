

n1 = 5
n2 = n1
n2 = n2 * 5

print(n2)

print(n1)

#vamos hacer lo mismo pero en listas

lista1 = [1,2]
lista2 = lista1.copy()

lista2[0] = lista2[0] * 5

print(lista2)

print(lista1)


#ojo con esto

# n1 == 5
# n2 == 25

#lista1 == 1 | 2
# lista2 == 5 | 2
