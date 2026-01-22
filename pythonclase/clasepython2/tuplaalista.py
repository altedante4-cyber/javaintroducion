"""
Docstring for tuplaalista
tupla a Lista
Básico
 Tuplas
 Conversión
Escribe una función que convierta una tupla en lista, modifique un elemento específico y la vuelva a convertir en tupla.
Requisitos:
Convertir tupla a lista
Recibir índice y nuevo valor como parámetros
Retornar nueva tupla modificada
Ejemplo:
modificar_tupla((1, 2, 3), 1, 99)
Output: (1, 99, 3)

"""

modificar_tupla=((1,2,3) , 1,99)

lista = list(modificar_tupla[0] )+ list(modificar_tupla[1:]) 



#tupla a lista


#pedir  indice y un nuevo valor como parametro
indice = int(input("INGRESE EL INDICE"))
valor_nuevo = int(input("Ingrese el nuevo valor"))


lista[indice] = valor_nuevo

print(lista)





