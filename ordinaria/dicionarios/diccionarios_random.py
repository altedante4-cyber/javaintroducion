import random

azar = {chr(65+i): random.randint(1, 100) for i in range(8)}
print("Aleatorios:", azar)

azar_ordenado = dict(sorted(azar.items(), key=lambda x: x[1]))
print("Ordenado:", azar_ordenado)

nombres = ["Ana", "Luis", "Carlos", "Marta"]
notas = {n: [random.randint(0, 10) for _ in range(3)] for n in nombres}
print("Notas aleatorias:", notas)

medias = {n: round(sum(v)/len(v), 2) for n, v in notas.items()}
print("Medias:", medias)

sorteo = dict(zip(nombres, random.choices(range(1, 50), k=len(nombres))))
print("Sorteo:", sorteo)

baraja = {f"{palo}_{num}" for palo in ["O", "C", "E", "B"] for num in range(1, 13)}
seleccion = dict(zip(random.sample(list(range(1, 49)), 5), ["rojo", "azul", "verde", "amarillo", "negro"]))
print("Seleccion aleatoria:", seleccion)
