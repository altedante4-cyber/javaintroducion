tupla1 = (1,2,3)

tupla2 = ("helena","jorge","ana")

tupla3 = ("jose maria",True , 57 , 1200 , 45 )

#es igual que los arra no puede agregar elementos , eliminar , ni modificar
#se utiliza cuando nose necesita modificar nada 

lista = [45.33,67.33,1200.44]

tupla4 = tuple(lista)

print(tupla4)

lista2= list(tupla2)
print(lista2)

texto =str(tupla1)

print(texto[1:-1])

#crear una tupla vacia
tuplavacia = ()
print(tuplavacia)


tuplaConUnElementoNo = ("Ana") #esto es un string no es una tupla

tuplaConUnElemento2 = ("Ana",) #indicar que es una tupla de un unico elemento 

print(tuplaConUnElementoNo)

#esto es una tupla de un uncio elemento

print(tuplaConUnElemento2)


#crear una tupla con un array dentro

tuplas5 = (1,"Ana" , [2,4,5])
print(tuplas5)

tuplas5[2].append(7)

print(tuplas5)

#====================================CONJUNTOS ==============================
conjunto1 = {"Ana","Pedro","Juan"}

conjunto2 = {1,33,56}

print(conjunto1)
print(conjunto2)

#no admite elementos repetidos

conjunto1.add("Pedro")
conjunto1.add("patricia")
conjunto1.add("michael")


print(conjunto1)

import random 

conjunto = set()

while len(conjunto) != 10 :

    conjunto.add(random.randint(1,10))

print(conjunto)

