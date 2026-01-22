
import random

#METODO EFICIENTE
#numeros = random.sample(range(1, 50), 6)  # 6 números únicos del 1 al 49

#print("Números de la lotería:", numeros)


numeros = []
for _ in range(6):
    nuevo = random.randint(1,49)

    for j in range(len(numeros)):

        if nuevo == numeros[j]:
            nuevo = random.randint(1,49)
            j = - 1   # reiniciamos el bucle interior 
            continue 

    # si pasamos el bucle sin repetir lo anadimos a la lista

    numeros.append(nuevo)

print(numeros)

cadena_nuva = ','.join(map(str,numeros))
print(cadena_nuva)


numero = input("introudce un numero : ")



print(
    f"{numero.count('8')} veces el número 8 \n"
    f"{numero.count('5')} veces el número 5 \n"
     f"{numero.count('3')} veces el número 3\n"
    f"{numero.count('2')} veces el número 2 \n"
      f"{numero.count('0')} veces el número 2 \n"
     )

# con un bucle for


for digitos in '0123456789':

   cantidad = numeros.count(digitos)

   if cantidad > 0 :
       
       if cantidad == 1 :
           print(f"{cantidad} número {digitos}")
       else:
            print(f"{cantidad} números {digitos}")


    





#188

