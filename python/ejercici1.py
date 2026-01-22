n = input("ingrese el numer").split()

conatdor_palabra = 0

for palabras in n :

    #contar vocales unicas en cada palabra

    vocales_unicas = set()
   

    for letra in palabras.lower():

        if letra in 'aeiou':

            vocales_unicas.add(letra)
if len(vocales_unicas) >= 4:

    conatdor_palabra+= 1 



    print(vocales_unicas)





















        




    
