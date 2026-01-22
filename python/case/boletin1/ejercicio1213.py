"""
Docstring for ejercicio1213

12. Escribir un programa que sirva como asistente para un juego de rol. Tu programa debería de
pedir por teclado el número de dados que se van a tirar y el número de caras de estos (4, 6,
8, 12, etc.) A continuación debería de hacer la tirada y mostrarla.


13. Modifica el programa anterior para que no admita dados con un número de caras impares
(¡no existen!). En el caso de meter un número impar de caras el programa debería de
informarnos de que es erróneo y volver a preguntarnos por este dato.


"""

import random 
valido = False 
while not valido :

   num_dado = int(input("ingrese el numero de daods que se van a tirar  "))
   num_caras = int(input("Ingrese el numero de caras que se van a tirar ")) #esto significa si el usuario ingresa 6 es que va  a lansar del 1 al 6

   if num_dado % 2 == 0 and num_caras % 2 == 0 :
       
       valido = True 
   else:
       print("!NO EXISTEN!")




    




i = 0 
while i < num_dado :

    print(random.randint(1,num_caras))


    i += 1 





