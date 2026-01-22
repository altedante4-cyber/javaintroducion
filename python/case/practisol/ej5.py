#Ruleta de Precios
#Define una lista de precios ([5, 10, 20, 50, 100]). Simula 5 turnos de ruleta. En cada turno, selecciona un precio aleatorio de la lista. Si el precio seleccionado es mayor que 30, imprime "¡Premio Mayor!". Al final, calcula e imprime la suma total de los precios obtenidos
import random

precios = [5, 10, 20, 50, 100]

contador = 0
sumador = 0

while contador < 5:
    precio_aleatorio = random.choice(precios)
    print(f"TURNO {contador + 1}: Precio seleccionado = {precio_aleatorio}")

    if precio_aleatorio > 30:
        print("¡Premio Mayor!")

    sumador += precio_aleatorio
    contador += 1

print(f"Suma total de precios obtenidos: {sumador}")
