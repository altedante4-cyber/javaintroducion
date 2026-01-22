import random


numeros_aleatorios = []
for i in range(50):

    num = random.randint(100,199)

    numeros_aleatorios.append(num)


#mostra los 50 numeros separados por espacios

print("Los 50 numeros aleatorios son :")
print(" ".join(str(num) for num in numeros_aleatorios))

#3 mostrar estadisticas

print(f"\nMinimo : {min(numeros_aleatorios)})")
print(f"\nMaximo : {max(numeros_aleatorios)})")
print(f"\n Media : {sum(numeros_aleatorios)/len(numeros_aleatorios)})")

