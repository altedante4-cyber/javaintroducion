"""
Docstring for ejercicio1415
14. Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
comprendido entre ambos. Por el momento no te preocupes de que el primer número
siempre debería de ser menor que el segundo, simplemente no los metas en un orden
incorrecto.
15. Modificar el programa del punto anterior para que si el primer número que metemos es
mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
50 y el 10 que no tiene mucha lógica…)

"""
import random

num1 = int(input("ingrese el numero"))
num2 = int(input("ingrese el segundo numero"))


if (num1 > num2 ):

    inicio = num2
    fin = num1
else:
    inicio = num1
    fin = num2 


print(random.randint(inicio,fin))



