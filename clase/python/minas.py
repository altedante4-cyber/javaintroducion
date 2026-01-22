import random

tab = [[0 for _ in range(5)] for _ in range(5)]

minas = 5
placed = 0

while placed < minas :

    f = random.randint(0,2)
    c = random.randint(0,2)

    if tab[f][c] == 0:

        tab[f][c] = 1

        placed += 1 

for fila in tab:
    print(fila)



