"""itertools: la navaja suiza de listas en Python"""

import itertools as it

# --- count(start, step): contador infinito ---
for i, val in zip(range(5), it.count(10, 2)):
    pass  # 10, 12, 14, 16, 18

# --- cycle: cicla infinitamente ---
list(zip(range(6), it.cycle(["A", "B", "C"])))
# [(0,A), (1,B), (2,C), (3,A), (4,B), (5,C)]

# --- repeat: repite un valor ---
list(it.repeat("x", 3))  # ['x', 'x', 'x']
# Útil con map: list(map(pow, range(1,5), it.repeat(2)))  # [1,4,9,16]

# --- chain: concatenar iterables ---
list(it.chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]
list(it.chain.from_iterable([[1, 2], [3, 4], [5]]))  # mismo, desde iterable

# --- accumulate: suma acumulada / reducción progresiva ---
list(it.accumulate([1, 2, 3, 4]))         # [1, 3, 6, 10]
list(it.accumulate([1, 2, 3, 4], func=pow))  # [1, 2, 8, 4096]

# --- product: producto cartesiano (como for anidados) ---
list(it.product([1, 2], ["a", "b"]))
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
list(it.product([1, 2], repeat=2))  # con sí mismo

# --- permutations / combinations ---
list(it.combinations_with_replacement([1, 2, 3], 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

# --- compress: filtrar con máscara booleana ---
list(it.compress("ABCDEF", [1, 0, 1, 0, 1, 0]))  # ['A', 'C', 'E']

# --- groupby: agrupar (requiere datos ordenados por clave) ---
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
groups = {k: list(g) for k, g in it.groupby(data, key=lambda x: x[0])}
# {'a': [('a',1), ('a',2)], 'b': [('b',3), ('b',4)]}

# --- islice: slicing perezoso (sin crear lista) ---
list(it.islice(range(100), 10, 20, 2))  # [10, 12, 14, 16, 18]

# --- batched (Python 3.12+): chunk sin copia ---
# list(it.batched(range(10), 3))  # [(0,1,2), (3,4,5), (6,7,8), (9,)]

# --- pairwise: pares consecutivos (Python 3.10+) ---
list(it.pairwise([1, 2, 3, 4]))  # [(1,2), (2,3), (3,4)]

# --- tee: múltiples iteradores desde uno ---
a, b = it.tee([1, 2, 3], 2)
list(a)  # [1, 2, 3]
list(b)  # [1, 2, 3] (independiente)

# --- starmap: map con desempaquetado ---
list(it.starmap(pow, [(2, 3), (3, 2)]))  # [8, 9]

# --- zip_longest: zip con relleno ---
list(it.zip_longest([1, 2], ["a"], fillvalue="?"))  # [(1,'a'), (2,'?')]
