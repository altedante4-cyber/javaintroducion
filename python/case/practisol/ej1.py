#Adivina el numero secreto
import random

num = random.randint(1,100)
print(num)

acertado = False

while not acertado:
    try:
        user = (int(input("ingrese un numero")))

        if user == num:

            acertado = True 
        elif user > num :
            print("Apunta mas bajo")
        else:
            print("apunta mas alto")


    except ValueError:

        print("Debe ingresar un numero valido ")
    
print("has acertado")