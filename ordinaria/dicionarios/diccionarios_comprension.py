nums = range(1, 11)
cuadrados = {n: n**2 for n in nums}
pares = {n: n**2 for n in nums if n % 2 == 0}
impares = {n: n**2 for n in nums if n % 2 != 0}

ciudades = ["Madrid", "Paris", "Londres", "Roma"]
longitudes = {c: len(c) for c in ciudades}

palabras = ["casa", "arbol", "sol", "elefante"]
agrupadas = {p: len(p) for p in palabras}
largas = {p: len(p) for p in palabras if len(p) > 3}

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
union = {**a, **b}
interseccion = {k: a[k] for k in a if k in b}

print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Impares:", impares)
print("Longitudes:", longitudes)
print("Largas:", largas)
print("Union:", union)
print("Interseccion:", interseccion)
