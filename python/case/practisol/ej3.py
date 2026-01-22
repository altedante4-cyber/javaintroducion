#simulacion de lanzamiento de dados
#simula 100 lanzamienots de un dado de 6 caras usa un bucle 
#for para generar 100 numeros aleatorios entre 1 y 6
#guarda los resultados en una lista y luego cuenta y muestra cuantas veces
#salio cada numero(1,2,3,4,5,6)

import random
#1 crea una lista vacia para guardar los resultados

resultado = []

#2 paso 3 crear un bucle for para simular 100 lanzamientos

for i in range(100):
#generar un numeros aleatorio entre 1 y 6
    lanzamiento = random.randint(1,6)
    resultado.append(lanzamiento)

#paso 5 contar cunatas veces salio cada numero 

for numero in range(1,7):

    cantidad = resultado.count(numero)
    print(f"El numero{numero} salio {cantidad} veces")

