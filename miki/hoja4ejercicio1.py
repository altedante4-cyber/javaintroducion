import random

numeros_set = set()

for i in range(6):
    num = random.randint(1,49)

    numeros_set.add(num)


for i in numeros_set:
    print(i)