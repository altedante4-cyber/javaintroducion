"""
Docstring for practica10
Contar en Tupla
Básico
 Tuplas
 Conteo
Escribe una función que cuente cuántas veces aparece un elemento específico en una tupla sin usar el método count().
Requisitos:
Recorrer la tupla manualmente
Contar apariciones del elemento buscado
Retornar el contador
Ejemplo:
contar((1, 2, 3, 2, 4, 2), 2)
Output: 3

"""


contar=(1, 2, 3, 2, 4, 2)

contador = 0

while True:
    try:

        numero_contar = int(input("ingrese el numero a contar"))


        if numero_contar < 0 :

            print("Error no se puede introducir numeros negativos ")
            continue
        break 
    except ValueError:
        print("Error ingrese un numero por favor  ")


    
for i in contar :

    if i == numero_contar:
        contador += 1 


print(contador)


