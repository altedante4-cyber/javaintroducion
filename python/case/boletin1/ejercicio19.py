"""
Docstring for ejercicio19
19. Escribir un programa que pida un número por teclado y nos muestre sus divisores

"""

num = int(input("ingrese el numero "))


i = 1

while i < num :

    if num % i == 0 :

        print(i)

    

    i += 1 
