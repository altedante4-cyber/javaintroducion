size = 4
for i in range(size):
    for j in range(size):
        # Si la suma de los índices es par, es un color; si es impar, otro.
        if (i + j) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()