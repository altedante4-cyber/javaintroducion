"""
Docstring for concatenartupla

Concatenar Tuplas
Básico
 Tuplas
 Concatenación
Crea una función que reciba múltiples tuplas como argumentos y las concatene en una sola tupla.
Requisitos:
Usar *args para recibir número variable de tuplas
Concatenar todas las tuplas recibidas
Retornar una sola tupla resultante
Ejemplo:
Input: (1, 2), (3, 4), (5, 6)
Output: (1, 2, 3, 4, 5, 6)

"""
tupla = (

    (1,2),
    (3,4),
    (5,6)

)

fusion = tupla[0] + tupla[1] + tupla[2]

print(fusion)

