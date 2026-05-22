"""Operaciones esenciales: slicing, unpacking, referencias, copy"""

# --- SLICING [start:stop:step] ---
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]        # [2, 3, 4]
nums[:4]         # primeros 4
nums[4:]         # desde índice 4
nums[::2]        # pares
nums[1::2]       # impares
nums[::-1]       # reverse (copia invertida)
nums[-3:]        # últimos 3
nums[:-3]        # todos menos últimos 3
nums[5:2:-1]     # [5, 4, 3]

# Reemplazo por slicing (muta la lista)
nums[3:5] = [30, 40]  # reemplaza posiciones 3 y 4
nums[3:5] = []        # elimina posiciones 3 y 4
nums[1:1] = [10, 20]  # inserta sin reemplazar

# --- UNPACKING ---
a, b, *resto = [1, 2, 3, 4, 5]  # a=1, b=2, resto=[3,4,5]
a, *medio, b = [1, 2, 3, 4, 5]  # a=1, medio=[2,3,4], b=5
primero, segundo, *_, ultimo = [1, 2, 3, 4, 5]

# Unpacking con * (en cualquier posición)
nueva = [0, *nums, 10]

# --- COPY (¡cuidado con referencias!) ---
original = [[1, 2], [3, 4]]
copia_superficial = original.copy()       # misma sublistas
copia_superficial2 = original[:]          # igual
copia_profunda = [list(sub) for sub in original]  # sublistas nuevas

import copy
copia_profunda2 = copy.deepcopy(original)

# --- enumerate + zip prácticos ---
# Índice y valor
for i, v in enumerate(["a", "b", "c"]):
    pass

# Paralelo con zip
for n, a in zip(nums, ["a", "b", "c"]):
    pass

# Desempaquetar argumentos con *
puntos = [(1, 2), (3, 4), (5, 6)]
xs, ys = zip(*puntos)  # xs=(1,3,5), ys=(2,4,6)

# --- reversed ---
list(reversed(nums))   # iterator, no muta
nums.reverse()         # in-place
nums[::-1]             # crea copia invertida
