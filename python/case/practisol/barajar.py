#barar cartas(simulacion)
#crea una lista que represente una pequena baraja de 5 cartas
#(por ejemplo, ["A", "K", "Q", "J", "10"]). Usa random.shuffle() para mezclar la lista. Luego, usa un bucle para mostrar las cartas en el nuevo orden.


import random
cartas = ['A','K','Q','J','10']

#mezclar esta mal por que shuffle mezcla la lista en su lugar y no devuelve nada
# por eso mezclar sera none
#lo correctos es simplemente llamar a random.shuffle(cfartas) sinasignarlo a otra variable
#mezclar = random.shuffle(cartas)

random.shuffle(cartas)

for i in cartas:
    print(i)
