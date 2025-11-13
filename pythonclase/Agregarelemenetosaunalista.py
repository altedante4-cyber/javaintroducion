import random

enteros = [1,2,3,4]

#estp agrega un  eleemtno sin mas
enteros.append(33)

print(enteros)


# insert anade a una determinada posicion

enteros.insert(2,777)
print(enteros)
# con esto le estamos diciendo agrega ese numero en una determinada posicion



# ejemplo de sumar cadenas


masEnteros = [6,7,8]

todosJUntos = masEnteros + enteros

print(todosJUntos) # esto te devuelve una nueva cadena  con las dos cadenas concatenadas


masEnteros.extend(enteros) # lo mismo que el concatenar
print(masEnteros)

numero = todosJUntos.pop() # me extrae esse numero  que se encuentra en esa posicion
print(todosJUntos)
print(numero)


numero = todosJUntos.pop(2) # ne estra el numero que se encuentra en esa posicion
print(todosJUntos)
print(numero)


#clera => elimina todos los elementos de una lista

numero = todosJUntos.clear()
print(todosJUntos)
print(numero)

#busca en la ista un determinado elemento y lo elimina

#numero = todosJUntos.remove(6) # nos da error por que el numero no aparece en la lista
print(todosJUntos)
print(numero)

#si existe mas de un eleemnto   elimina el primero que aparece

enteros = [1,22,3,12]
masEnteros = [61,33,7,13,8]


todosJUntos = masEnteros + enteros
print("segunda parte")
print(todosJUntos)
todosJUntos.sort() # ordenamos la lista
print(todosJUntos)
todosJUntos.sort(reverse=True) # ordenamos la lista en orden descendente
print(todosJUntos)



letras = ["Ana" , "pepe" , "Juan"]
print("segunda parte")
print(letras)
letras.sort() # ordenamos la lista
print(letras)
letras.sort(reverse=True)
print(letras)

#ojo cuidado la  mayuscula y minuscula no  funciona  la mayusculs van primero antesque las minusculas
# primero mayusculas,minuscula , numeros

letras = ["Ana" , "pepe" , "Juan",33]
print("segunda parte")
print(letras)
#letras.sort() # ordenamos la lista
print(letras)
#letras.sort(reverse=True)
print(letras)



# BUSCAR SI UN ELEMENTO ESTA EN LA LISTA

if "pepe" in letras:
    print("ee esta en la lista ")
else:
    print("no esta ")

#Preguto si no esta con

if "pepe" not in letras:
    print("pepe no esta en la lista")
else:
    print("si que esta ")


# ademas necesito saber su posicion


posicion = letras.index("pepe") # si no esta te devuleve un error
print(posicion)


#para saber el numero de veces que aparece un elemento en la lista
veces =letras.count(33)
print(veces)



#inicialisar una lista de la fomra mas rapida

ejemplo = ["Ana" , "Pepe","Juan"]

secuencia = [i for i in range(2,50,2)]
print(secuencia)


#otro mas bonito

secuecia2 = [random.randint(1,6 ) for _ in range(0,10)]
print(secuecia2)