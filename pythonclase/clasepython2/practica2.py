"""
Docstring for practica2

2. Eliminar duplicados
Dada una lista [1, 2, 2, 3, 4, 4, 5], conviértela en conjunto para eliminar duplicados y luego vuelve a convertirla en lista ordenada.
"""
lista = [1,2,2,3,4,4,5]


conjunto_noduplicada = set()


for i in lista:

    conjunto_noduplicada.add(i)



#ya tenmos creado el conjunto sin duplicados ahora hay convertir a una lista ordenada


lista_ordenada = []



for i in conjunto_noduplicada:

    lista_ordenada.append(i)




print(lista_ordenada)
