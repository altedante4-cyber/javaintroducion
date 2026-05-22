"""filter, map, reduce, any, all — funcionales sin loop explícito"""

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- map: transforma cada elemento ---
cuadrados = list(map(lambda x: x ** 2, nums))
# Equivalente: [x ** 2 for x in nums]

# --- filter: selecciona según condición ---
pares = list(filter(lambda x: x % 2 == 0, nums))
# Equivalente: [x for x in nums if x % 2 == 0]

# --- reduce: acumula (reduce a un solo valor) ---
suma = reduce(lambda acc, x: acc + x, nums, 0)
producto = reduce(lambda acc, x: acc * x, nums, 1)
maximo = reduce(lambda a, b: a if a > b else b, nums)

# --- any / all: check booleano sobre iterables ---
hay_par = any(x % 2 == 0 for x in nums)
todos_pares = all(x % 2 == 0 for x in nums)
ninguno_negativo = not any(x < 0 for x in nums)

# --- zip: empareja múltiples listas ---
nombres = ["Ana", "Luis", "Eva"]
edades = [25, 30, 22]
personas = list(zip(nombres, edades))  # [("Ana",25), ("Luis",30), ("Eva",22)]

# Desempaquetar con zip (transponer)
pares = [(1, 4), (2, 5), (3, 6)]
a, b = zip(*pares)  # a = (1,2,3), b = (4,5,6)

# --- enumerate: índice y valor ---
for i, nombre in enumerate(nombres, start=1):
    pass  # i empieza en 1

# --- Combinaciones poderosas ---
# Suma de cuadrados de pares
resultado = sum(x ** 2 for x in nums if x % 2 == 0)

# Promedio con reduce
promedio = reduce(lambda acc, x: acc + x, nums, 0) / len(nums)

# Máximo con reduce y key (como max(..., key=...))
palabras = ["casa", "arbol", "sol", "edificio"]
mas_larga = reduce(lambda a, b: a if len(a) > len(b) else b, palabras)
