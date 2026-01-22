"""
10. Escribir un programa que genere dos números aleatorios simultáneamente entre el 1 y el 6
(simulando una tirada de dos dados)


11. Modificar el programa anterior para que tu programa tire dos dados de forma continuada
hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado

"""
import random 

contador = 0 
acertado = False 
while not acertado:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    if(dado1 != dado2 ):

        contador += 1
    else:

        print("acertado")
        acertado = True  

print(f"has tenido que fallar {contador} para hacertar")