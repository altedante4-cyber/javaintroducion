"""List comprehensions: forma más pythonica de crear/transformar listas"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Básica: [expr for item in iterable]
cuadrados = [n ** 2 for n in nums]

# Con condición: [expr for item in iterable if cond]
pares = [n for n in nums if n % 2 == 0]

# Con condición doble: expr_if if cond else expr_else
par_impar = ["par" if n % 2 == 0 else "impar" for n in nums]

# Anidada (equivalente a flatten)
matriz = [[1, 2], [3, 4], [5, 6]]
plana = [num for fila in matriz for num in fila]

# Con enumerate para índice y valor
indices_pares = [i for i, n in enumerate(nums) if n % 2 == 0]

# Set comprehension (misma sintaxis, llaves)
{n % 3 for n in nums}

# Dict comprehension
{n: n ** 2 for n in nums if n % 2 == 0}

# Anidamiento real (producto cartesiano)
colores = ["rojo", "azul"]
items = ["coche", "casa"]
combinaciones = [f"{c} {i}" for c in colores for i in items]

# flatten de listas irregulares con recursividad (no trivial)
def flatten(lst):
    return [x for sub in lst for x in (flatten(sub) if isinstance(sub, (list, tuple)) else [sub])]

anidada = [1, [2, [3, 4]], 5]
print(flatten(anidada))  # [1, 2, 3, 4, 5]
