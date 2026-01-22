import random 

#8. Llenar una Lista con Pares/Impares 🔢
#Inicializa una lista vacía. Usa un bucle while para añadir 15 números enteros aleatorios entre 1 y 50 a la lista. Después de llenar la lista, usa otro bucle for y una condicional (if) para contar y mostrar cuántos números son pares y cuántos son impares.


pares = [random.randint(1,50) for _ in range(15)]


contador_pares = 0 
contador_inpares = 0 


for n in pares:
    if n % 2 == 0:
        contador_pares += 1 
    else:
        contador_inpares += 1

    

print("Listta generada" , pares)
print("cantidad de pares" ,contador_pares)
print("cantidad de inpares" , contador_inpares)
 