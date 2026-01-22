

#materia = ["Matematicas",'FIsica','Quimica' , "historia", "Lengua "]
##notasa = []

##for index,materias  in enumerate(materia):

  ##  n = int(input("Ingrese la nota que has sacado en " + materias ))
    
   ## notasa.append(n)


##print(materia)
##print(notasa)



#for i,j in zip(materia,notasa):

 #   print(i , "==" , j )



""" 
# Dada una lista, suma solo los números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Resultado esperado: 30 (2+4+6+8+10)

suma = 0 
for  i , namber in enumerate(numeros):

    if namber % 2 == 0 :
        
        suma += namber 


print(suma)



"""


"""
encontrar el maximo y minimom 
# Crea una función que encuentre el número más grande y el más pequeño
# SIN usar max() o min()
lista = [12, 45, 2, 78, 5, 91, 23]
# Resultado: (91, 2)






maximo = lista[0]
minimo = lista[0]
for i in range(len(lista)):

    if lista[i] > maximo :

        maximo = lista[i]
    elif lista[i] < minimo :

            minimo = lista[i] 

print(maximo)
print(minimo)
"""

"""

eliminar duplicados 
# Dada una lista con elementos repetidos, crea una nueva sin duplicados
lista = [1, 2, 2, 3, 4, 4, 4, 5, 1]
# Resultado: [1, 2, 3, 4, 5]



# Dada una lista con elementos repetidos, crea una nueva sin duplicados
lista = [1, 2, 2, 3, 4, 4, 4, 5, 1]
# Resultado: [1, 2, 3, 4, 5]

lista_sin_duplicados = []

for i in range(len(lista)):

    if lista[i] not in lista_sin_duplicados:

        lista_sin_duplicados.append(lista[i])
    


print(lista_sin_duplicados)


"""



"""
4.contador de palabras 

# Dada una lista de palabras, cuenta cuántas veces aparece cada una
palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
# Resultado: {"hola": 3, "mundo": 2, "python": 1}


# Dada una lista de palabras, cuenta cuántas veces aparece cada una
palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
# Resultado: {"hola": 3, "mundo": 2, "python": 1}



contador = {}

for palabra in palabras :

    if palabra in contador:

        contador[palabra] += 1
    else:

        contador[palabra] = 1 

print(contador)
"""


"""
fusionar y ordenar listas

# Dadas dos listas ordenadas, fusionarlas en una sola lista ordenada
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8]

"""
"""
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8]


numeros_ordenador = lista1 + lista2 


n = len(numeros_ordenador)



for i in range(n):
    for j in range(0,n -i-1):

        if numeros_ordenador[j] > numeros_ordenador[j+1]:

            temp = numeros_ordenador[j]
            numeros_ordenador[j] = numeros_ordenador[j+1]
            numeros_ordenador[j+1] = temp
        

print(numeros_ordenador)

# 0 empezamos desde el primer indice
# n-i-1 => hasta el indice antes del ultimo elemento sin ordenar
# por que n-i-1:
# depsues de la primera pasada el ultimo elemnto est en su posicioin co

   
    
"""

"""
# Encuentra los elementos que están en ambas listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
# Resultado: [4, 5]

lista_igaul = []


for i in range(len(lista1)):

    for j in range(len(lista2)):

        if lista1[i] == lista2[j]:

            lista_igaul.append(lista1[i])
            

print(lista_igaul)
"""

"""
# Rota una lista N posiciones a la derecha
lista = [1, 2, 3, 4, 5]
n = 2
# Resultado: [4, 5, 1, 2, 3]


texto = lista[:-2]

print(texto)

texto2 = lista[-2:]

print(texto2)


# con un bucle for 

for _ in range(n): #repetinos n veces

    temp = lista[-1] # guadamos el ultimo elemento 

    for i in range(len(lista)-1,0,-1):  
        lista[i] = lista[i-1] # movemos cada elemento una posicion  a la izquierda
    
    lista[0] = temp        # colocamos el ultimo eleemetno al iinicio

print(lista)

"""



"""
creacion y modificacion de listas
Crea una lista vacía y añade los números del 1 al 10 usando un bucle for.

Elimina todos los elementos pares de la lista usando un bucle while.

Reemplaza cada elemento por su cuadrado usando un bucle for con enumerate().

"""

""" 
lista_vacia = []

for i in range(1,11):

    lista_vacia.append(i)


x = 0 
while  x < len(lista_vacia):
    
     if lista_vacia[x] % 2 == 0 : 
        lista_vacia.pop(x)
     else:

         x += 1 

print(lista_vacia)
  


for i, numero in enumerate(lista_vacia):

     lista_vacia[i] = numero ** 2 


print(lista_vacia)
"""


"""
numeros = [10, 25, 30, 45, 50, 65, 70, 85, 90]


for i in range(len(numeros)):

    if numeros[i] % 5 == 0 :

        print(numeros[i]) 

print("-----------------------------")
x = 0 
while x < len(numeros):

     if numeros[x] > 60:
         print(numeros[x])
         break;
         

     x += 1


print("---------------------")

suma = 0 
for i in range(len(numeros)):

    if numeros[i] > 20 and numeros[i] < 80 :

             suma += 1 
    
print(suma)

"""

"""

Ejercicio 3: Manipulación con bucles anidados
Dada la lista de listas:

python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Imprime cada elemento usando bucles anidados.

Calcula la suma de todos los elementos usando bucles anidados.

Crea una nueva lista con los elementos pares de toda la matriz.



matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = 0 

pares_matriz = []
for i in range(len(matriz)):

    for j in range(len(matriz)):
  
           suma += matriz[i][j]


print(suma)


for i in range(len(matriz)):
      for j in range(len(matriz)):
            
            if matriz[i][j] % 2 == 0 :
                  
                  pares_matriz.append(matriz[i][j])

print(pares_matriz)



"""

"""
Ejercicio 4: Filtrado con list comprehensions
Crea una lista con los cuadrados de los números del 1 al 15.

Filtra solo los números pares de la lista anterior.

Crea una lista de tuplas (número, cuadrado) para los números del 1 al 10.

numeros = []


for i in range(1,16):

    numeros.append(i ** 2 )


#filtramos solo los numeros pares


for i in range(len(numeros)):

    if numeros[i] % 2 == 0 :

        print(numeros[i])


# crae una lista de tuplas (numeros,cuadrado) para los nuemros del 1 al 10 


lista_tuplas = []

# recorremos los numeors del 1 al 10 
for n in range(1,11):
    # creamos la tupla(nummero ,cuadrado ) y la agreaamos a la lista

    lista_tuplas.append((n,n ** 2 ))


#mostraros la lista de tuplas


print(lista_tuplas)

"""
"""
Ejercicio 5: Operaciones con rangos y bucles
Usa range() para crear una lista de números del 0 al 100 con paso 5.

Usa un bucle for para sumar todos los números pares entre 1 y 50.

Crea una lista inversa usando range() con paso negativo.


lista_numeros = []
for i in range(0 , 101 , 5 ):

    lista_numeros.append(i)


print(lista_numeros)



suma = 0 

for i in range(min(51,len(lista_numeros))):

    if lista_numeros[i] % 2 == 0:

        suma += lista_numeros[i]

print(suma)


# creamos la lista inversa 

for i in range(len(lista_numeros)-1,-1,-1 ):

    print(lista_numeros[i])
    


for num in lista_numeros[::-1]:
    print(num)
"""


"""
Ejercicio 6: Modificación in-place
Dada la lista:
palabras = ["casa", "perro", "gato", "sol", "agua"]

"""

"""
palabras = ["casa", "perro", "gato", "sol", "agua"]


for i in palabras:

    mayuscula = i.upper()
    print(mayuscula)


x = 0 
while x < len(palabras):

    if palabras[x].count() 


"""


