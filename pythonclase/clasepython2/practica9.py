"""
Docstring for practica9
Acceso a Tuplas
Básico
 Tuplas
 Acceso
Crea una función que reciba una tupla de al menos 5 elementos y retorne el primer, tercer y último elemento en una nueva tupla.
Requisitos:
Usar indexación para acceder a elementos
Validar que la tupla tenga al menos 5 elementos => if not len(tupla) >= 5 
Retornar una nueva tupla con los elementos solicitados =>nueva_tupla 
Ejemplo:
Input: (10, 20, 30, 40, 50)
Output: (10, 30, 50)

"""


tupla = tuple(int(input("Ingrese numeros ")) for i in range(5))

print(tupla)

#sacar el primer elemento  , tercer , ultimo elemento




print(tupla[0])  # primer elemento
print(tupla[2])  # tercer elemento
print(tupla[-1]) 