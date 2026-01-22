import random

intentos = 5
numero_adivinado = False
numero_adivinar = random.randint(1, 100)
print(numero_adivinar)
while intentos > 0 and not numero_adivinado:

    numero_usuario = int(input("Ingrese un numero: "))

    if numero_usuario == numero_adivinar:
        numero_adivinado = True
    elif (numero_usuario < numero_adivinar):
         print("El numero es mayor ")
         intentos -= 1
    else:
        print("El numero es menor ")
        intentos -= 1

if numero_adivinado:
    print("El numero es adivinado ")
else:
    print("Se ha acabo su partida")