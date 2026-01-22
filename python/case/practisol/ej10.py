#10. Desafío de Ordenación Parcial 🔄
#Crea una lista de 8 números enteros aleatorios entre 1 y 50. Itera sobre la lista. Si un número es mayor que 30, reemplázalo por un nuevo número aleatorio entre 1 y 5. Si no, déjalo como está. Imprime la lista original y la lista modificada.


import random 

numeros = [random.randint(1,50) for _ in range(8)]
print(numeros)

lista_modificada = []
for i in numeros:

    if i > 30 :

        lista_modificada.append(random.randint(1,5))
    else:

        lista_modificada.append(i)


print(lista_modificada)

#definir el objetivo final 
#preguntate que debe hacer mi programa final?
#mostrarme todos los numeros que no sean mayores a 30


#patron2.indentificar las tareas grandes
#piensa en "accinoes gerales" que deben occurrir
#ejemplo:
# paso 1 iterar sobre la lista ya genereda de numeros aleatorios
# paso 2 filtracion los que sean mayores que 30 se quitan y se genera nuevos
#numeros aleatorias que esten dentro del rango 1 y 5
# paso 3 agregar a una nueva lista
#paso 4 mostrar


#🔹 Resumen completo de la descomposición

#Objetivo final: Mostrar lista modificada con números >30 reemplazados por 1–5.

#Tareas grandes: Iterar, filtrar, reemplazar, agregar a nueva lista, mostrar.

#Subproblemas: Revisar cada número, decidir si reemplazar, agregar a lista final.
#
#Condiciones especiales: Reemplazo solo si número > 30.

#Bucle necesario: for para iterar sobre 8 números.

#Almacenar resultados: Lista modificada.

#Construir paso a paso: Lista original → iterar → modificar → imprimir.

#Verificar resultado: Comparar lista original y modificada.