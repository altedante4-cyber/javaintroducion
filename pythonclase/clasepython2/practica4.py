"""
Docstring for practica4

4. Modificar lista dentro de tupla
Crea una tupla que contenga una lista, similar a tuplas5 del ejemplo. Luego:

Agrega dos elementos a la lista interna

Elimina un elemento específico de la lista

Convierte la lista en tupla dentro de la tupla principal


"""



tuplas5 = (1,"Ana" , [2,4,5])

tuplas5[2].append(9)
tuplas5[2].append(4)


tuplas5[2].remove(2)

#manera 1 de hacerlo expandir la lista interna dentro de la tupla

tuplas5 = (tuplas5[0],tuplas5[1],*tuplas5[2])


print(tuplas5)

#desempaquetar los elementos y reconstruir

a, b, *lst = tuplas5
tuplas5 = (a, b, *lst)
print(tuplas5)


