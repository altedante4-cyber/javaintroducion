import random

suma = 0
for i in range(3):

    dado = random.randint(0,10)
    suma += dado

    print(f"dado {i + 1} tienee el numero: {dado} ")
print(suma)