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


#en los conjunto no se en que poscion esta

#eliminar un conjunto remove 

print(conjunto1.remove("Ana")) # si no existe provoca una exepcion
print(conjunto1.discard("Ana"))# no provoca una excepcepcion si no existe


print(conjunto1.pop()) #elimina elementos al azar pero en veldad coge eleementos del principio


print(conjunto1)

#para limpiar completamente  utilizamos el conjunto 

conjunto.clear();

print(conjunto1)

lista1 = [1,33,2,1,2,33,42,33,1,25,5,1,33,2]
#convertimos a conjunto  > luego convvertimos a lista y luego nos quitamos los duplicados


conjunto3 = set(lista1)

lista1= list(conjunto3)

print(lista1)

profes1 = {"Yago","Natalia","Jose Maria","Paul","Eduardo","Javier"}
profes2 = {"Natalia","Puche","Jose Maria","Ana Maria","Israel"}

profesComun = profes1 & profes2 

print(profesComun) # cuando tenemos que enocntrar elementos comunes entre dos listas


