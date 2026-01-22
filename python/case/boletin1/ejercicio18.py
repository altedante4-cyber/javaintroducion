"""
Docstring for ejercicio18
18. Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que sólo
se detenga cuando salga el 666. Los números que ha tenido que generar tu programa hasta
aparecer el 666 son los que restan para el apocalipsis. Tu programa debería de indicarlo con
un mensaje tétrico (¡Faltan 236 días para que se acabe todo! por ejemplo)


"""

import random

encontrado = False 

contador = 0
while not encontrado:

    a = random.randint(1,1000)


    if a == 666 :

        encontrado = True
    else:

        contador += a 


print(f"!Faltan {contador} dias para que se acab todo ")