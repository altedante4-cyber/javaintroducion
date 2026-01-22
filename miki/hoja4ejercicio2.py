num1 = int(input())
num2 = int(input())


#hay que sacar los divisores comunes que tienen dichos numeros

numeros_1 = set()
numeros_2 = set()


for i in range(1 , num1 + 1):
    if num1 % i == 0 :
        numeros_1.add(i)

for i in range(1,num2 + 1):
    if num2 % i == 0 :
        numeros_2.add(i)


for i in numeros_1 :

    if i in numeros_2 :
        print(i)

