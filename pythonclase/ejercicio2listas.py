import random

lista = ["Pepe" , "Ana" , "Victor" , "Juan", "Eva"]


print(random.choice(lista)) #eleigmos un elemento alazar de una lista

print(random.sample(lista,6)) # coge elementos no repetidos  recoge eleimitods sin repeticion





random.shuffle(lista)
print(lista) # lo mismo que poner el smaple me ordena la misma lista pero ordenador de forma aleatoria


